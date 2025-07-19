import pytest
import random
from datetime import datetime, timedelta, timezone
from webportal.client_api.what_to_watch.assertions import WhatToWatchAssertions
from webportal.client_api.what_to_watch.locators import WhatToWatchLocators
from webportal.client_api.what_to_watch.labels import WhatToWatchLabels
from webportal.test_settings import WebPortalSettings as Settings
from webportal.factory.factory import Factory
import pprint


@pytest.fixture(scope="function")
def setup_what_to_watch(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.wtw_page = Factory.page_factory(request.cls)
    request.cls.wtw_assertions = Factory.assertions_factory(request.cls)


@pytest.fixture(autouse=False, scope="function")
def setup_what_to_watch_delete_subscriptions(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_what_to_watch_delete_subscriptions - method :::::::::::: \n")
    request.cls.api.delete_all_subscriptions()


@pytest.fixture(autouse=False, scope="function")
def setup_cancel_all_recordings(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_cancel_all_recordings - method :::::::::::: \n")
    request.cls.api.cancel_all_recordings()


@pytest.fixture(autouse=False, scope="function")
def setup_what_to_watch_create_OnePass(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_what_to_watch_create_OnePass - method :::::::::::: \n")
    request.cls.wtw_page.select_button_sign_in()
    request.cls.wtw_page.log_in()
    request.cls.wtw_assertions.mainPageTabs_assert()
    request.cls.wtw_page.go_to_What_to_Watch()
    request.cls.wtw_page.select_tile_from_strip()
    request.cls.log.info(" === Create OnePass ===")
    request.cls.wtw_page.select_Get_this_Show()
    request.cls.wtw_assertions.assert_Get_this_Show_displayed()
    request.cls.wtw_page.select_create_OnePass_option()
    request.cls.wtw_assertions.assert_OnePass_Options_displayed()
    request.cls.wtw_page.select_create_OnePass_button()
    request.cls.wtw_assertions.assert_Create_Whisper_OnePass()
    request.cls.log.info(" === OnePass Successfully created ===")


@pytest.fixture(autouse=False, scope="function")
def setup_login(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_login - method :::::::::::: \n")
    request.cls.wtw_page.select_button_sign_in()
    request.cls.wtw_page.log_in()
    request.cls.wtw_assertions.mainPageTabs_assert()
    request.cls.wtw_page.go_to_What_to_Watch()
    request.cls.wtw_page.select_tile_from_strip()


def get_time_interval(request, hours_interval):
    request.cls.log.info("I'm in get_time_interval() function.")
    past_hours = 4 + random.randint(0, 8)
    past_hours_timedelta = timedelta(hours=past_hours)
    showtime = datetime.strptime(request.cls.service_api.get_middle_mind_time(Settings.tsn)["currentTime"],
                                 '%Y-%m-%d %H:%M:%S') - past_hours_timedelta
    minEndTime = str(showtime)
    maxStartTime = str(showtime + timedelta(hours=hours_interval))
    request.cls.log.info(f"\n\n\t\tWILL SEARCH FOR SHOWS BETWEEN {minEndTime} and {maxStartTime}. "
                         f"past_hours_timedelta = {past_hours_timedelta}\n")
    return minEndTime, maxStartTime


@pytest.fixture(autouse=False, scope="function")
def setup_get_movie(request):
    request.cls.log.info(":::::::::::: PRECONDITION START: I'm in setup_get_movie() ::::::::::::")
    request.cls.log.info("")

    minEndTime, maxStartTime = get_time_interval(request, 24)
    grid_row = request.cls.service_api.get_grid_row_search(count=50, offset=0, collectionType='movie',
                                                           mindEndTime=minEndTime,
                                                           maxStartTime=maxStartTime)['gridRow']
    filtered_shows_list = request.cls.service_api.extract_offer_show(grid_row, 'movie', count=50)
    if filtered_shows_list is None:
        request.cls.log.error("Could not get any movie. SKIP TEST.")
        pytest.skip("Could not get any movie. SKIP TEST.")

    request.cls.log.info(f"Got {len(filtered_shows_list)} movie shows from PGD:\n {filtered_shows_list}\n")

    found = False
    for index in range(0, len(filtered_shows_list)):
        request.cls.log.info(f"Validate title '{filtered_shows_list[index][0]}' received from PGD.\n")
        unified_results = request.cls.service_api.unified_item_search(count=1, offset=0,
                                                                      keyword=filtered_shows_list[index][0])
        request.cls.log.info(f"Unified Item Search Result:\n{pprint.pformat(unified_results)}")

        if unified_results.get('unifiedItem'):
            result = unified_results['unifiedItem'][0]['title']
            request.cls.log.info(f"=== Compare movie from PGD '{filtered_shows_list[index][0]}' "
                                 f"with movie from unifiedItemSearch '{result}' ===")
            if filtered_shows_list[index][0] == result:
                request.cls.movie = filtered_shows_list[index][0]
                request.cls.movie_year = filtered_shows_list[index][1]
                found = True
                request.cls.log.info(f"For current box TSN {Settings.tsn} a valid movie was found: {request.cls.movie}")
                break

    if not found:
        request.cls.log.error("Could not get any movie. SKIP TEST.")
        pytest.skip("Could not get any movie. SKIP TEST.")

    request.cls.log.info("")
    request.cls.log.info(":::::::::::: PRECONDITION END: Exit from setup_get_movie() ::::::::::::")


@pytest.fixture(autouse=False, scope="function")
def setup_get_episodic(request):
    request.cls.log.info(":::::::::::: PRECONDITION START: I'm in setup_get_episodic() ::::::::::::")
    request.cls.log.info("")

    minEndTime, maxStartTime = get_time_interval(request, 24)
    grid_row = request.cls.service_api.get_grid_row_search(count=50, offset=0, collectionType='series',
                                                           mindEndTime=minEndTime,
                                                           maxStartTime=maxStartTime)['gridRow']
    filtered_shows_list = request.cls.service_api.extract_offer_show(grid_row, 'episodic', count=50)
    if filtered_shows_list is None:
        request.cls.log.error("Could not get any episodic. SKIP TEST.")
        pytest.skip("Could not get any episodic. SKIP TEST.")

    request.cls.log.info(f"Got {len(filtered_shows_list)} episodic shows from PGD:\n {filtered_shows_list}\n")

    found = False
    for index in range(0, len(filtered_shows_list)):
        request.cls.log.info(f"Validate title '{filtered_shows_list[index][0]}' received from PGD.\n")
        unified_results = request.cls.service_api.unified_item_search(count=1, offset=0,
                                                                      keyword=filtered_shows_list[index][0])
        request.cls.log.info(f"Unified Item Search Result:\n{pprint.pformat(unified_results)}")

        if unified_results.get('unifiedItem'):
            result = unified_results['unifiedItem'][0]['title']
            request.cls.log.info(f"=== Compare episodic from PGD '{filtered_shows_list[index][0]}' "
                                 f"with episodic from unifiedItemSearch '{result}' ===")
            if filtered_shows_list[index][0] == result:
                request.cls.episodic = result
                found = True
                request.cls.log.info(f"For current box TSN {Settings.tsn} a valid episodic was found: {request.cls.episodic}")
                break

    if not found:
        request.cls.log.error("Could not get any episodic. SKIP TEST.")
        pytest.skip("Could not get any episodic. SKIP TEST.")

    request.cls.log.info("")
    request.cls.log.info(":::::::::::: PRECONDITION END: Exit from setup_get_episodic() ::::::::::::")


@pytest.fixture(autouse=False, scope="function")
def setup_get_nonepisodic(request):
    request.cls.log.info(":::::::::::: PRECONDITION START: I'm in setup_get_nonepisodic() ::::::::::::")
    request.cls.log.info("")

    minEndTime, maxStartTime = get_time_interval(request, 24)
    grid_row = request.cls.service_api.get_grid_row_search(count=50, offset=0, collectionType='special',
                                                           mindEndTime=minEndTime,
                                                           maxStartTime=maxStartTime)['gridRow']
    filtered_shows_list = request.cls.service_api.extract_offer_show(grid_row, 'nonepisodic', count=50)
    if filtered_shows_list is None:
        request.cls.log.error("Could not get any nonepisodic. SKIP TEST.")
        pytest.skip("Could not get any nonepisodic. SKIP TEST.")

    request.cls.log.info(f"Got {len(filtered_shows_list)} nonepisodic shows from PGD:\n {filtered_shows_list}\n")

    found = False
    for index in range(0, len(filtered_shows_list)):
        request.cls.log.info(f"Validate title '{filtered_shows_list[index][0]}' received from PGD.\n")
        unified_results = request.cls.service_api.unified_item_search(count=1, offset=0,
                                                                      keyword=filtered_shows_list[index][0])
        request.cls.log.info(f"Unified Item Search Result:\n{pprint.pformat(unified_results)}")

        if unified_results.get('unifiedItem'):
            result = unified_results['unifiedItem'][0]['title']
            request.cls.log.info(f"=== Compare nonepisodic from PGD '{filtered_shows_list[index][0]}' "
                                 f"with nonepisodic from unifiedItemSearch '{result}' ===")
            if filtered_shows_list[index][0] == result:
                request.cls.nonepisodic = result
                found = True
                request.cls.log.info(f"For current box TSN {Settings.tsn} a valid nonepisodic was found:"
                                     f" {request.cls.nonepisodic}")
                break

    if not found:
        request.cls.log.error("Could not get any nonepisodic. SKIP TEST.")
        pytest.skip("Could not get any nonepisodic. SKIP TEST.")

    request.cls.log.info("")
    request.cls.log.info(":::::::::::: PRECONDITION END: Exit from setup_get_nonepisodic() ::::::::::::")


@pytest.fixture(autouse=False, scope="function")
def setup_get_series(request):
    """
    This function will extract from PGD (by using gridRow Search) 50 Offers that can contain
    less or more then 50 shows titles. This shows may not be found in a direct search in webportal UI.
    Therefore, the shows from that list are validated one by one using same search query used on webportal till one title
    is found valid.
    :param request:
    :return:
    """
    request.cls.log.info(":::::::::::: PRECONDITION START: I'm in setup_get_series() ::::::::::::")
    request.cls.log.info("")

    minEndTime, maxStartTime = get_time_interval(request, 24)
    grid_row = request.cls.service_api.get_grid_row_search(count=50, offset=0, collectionType='series',
                                                           mindEndTime=minEndTime,
                                                           maxStartTime=maxStartTime)['gridRow']
    filtered_shows_list = request.cls.service_api.extract_offer_show(grid_row, 'series', count=50)
    if filtered_shows_list is None:
        request.cls.log.error("Could not get any series. SKIP TEST.")
        pytest.skip("Could not get any series. SKIP TEST.")

    request.cls.log.info(f"Got {len(filtered_shows_list)} series shows from PGD:\n {filtered_shows_list}\n")

    found = False
    for index in range(0, len(filtered_shows_list)):
        request.cls.log.info(f"Validate title '{filtered_shows_list[index][0]}' received from PGD.\n")
        unified_results = request.cls.service_api.unified_item_search(count=1, offset=0,
                                                                      keyword=filtered_shows_list[index][0])
        request.cls.log.info(f"Unified Item Search Result:\n{pprint.pformat(unified_results)}")

        if unified_results.get('unifiedItem'):
            result = unified_results['unifiedItem'][0]['title']
            request.cls.log.info(f"=== Compare series from PGD '{filtered_shows_list[index][0]}' "
                                 f"with series from unifiedItemSearch '{result}' ===")
            if filtered_shows_list[index][0] == result:
                request.cls.series = result
                found = True
                request.cls.log.info(f"For current box TSN {Settings.tsn} a valid series was found: {request.cls.series}")
                break

    if not found:
        request.cls.log.error("Could not get any series. SKIP TEST.")
        pytest.skip("Could not get any series. SKIP TEST.")

    request.cls.log.info("")
    request.cls.log.info(":::::::::::: PRECONDITION END: Exit from setup_get_series() ::::::::::::")


@pytest.fixture(autouse=False, scope="function")
def setup_get_person(request):
    request.cls.log.info(":::::::::::: PRECONDITION START: I'm in setup_get_person() ::::::::::::")
    request.cls.log.info("")

    person_list_pgd = request.cls.service_api.get_person_search(Settings.tsn)
    if not person_list_pgd.get('person'):
        request.cls.log.error("Could not get any person. SKIP TEST.")
        pytest.skip("Could not get any person. SKIP TEST.")

    person_list = []
    for index in range(0, len(person_list_pgd['person'])):
        person_list.append(person_list_pgd['person'][index]['first'] + " " + person_list_pgd['person'][index]['last'])
    request.cls.log.info(person_list)

    found = False
    for index in range(0, len(person_list_pgd['person'])):
        person_pgd = person_list[index]
        request.cls.log.info("")
        request.cls.log.info(f"=== Validate person '{person_pgd}' received from PGD.===\n")
        unified_results = request.cls.service_api.unified_item_search(count=1, offset=0, keyword=person_pgd)
        request.cls.log.info(f"=== Unified Item Search Result: ===\n{pprint.pformat(unified_results)}")

        # Check to be a person and not a movie or other kind of show...
        if unified_results.get('unifiedItem'):
            if unified_results['unifiedItem'][index].get('type') == 'person':
                first = unified_results['unifiedItem'][index]['first']
                last = unified_results['unifiedItem'][index]['last']
                person_uis = first + " " + last

                request.cls.log.info(f"=== Compare person from PGD '{person_pgd}' with person from unifiedItemSearch"
                                     f" '{person_uis}' ===")
                if person_pgd == person_uis:
                    request.cls.person = person_uis
                    found = True
                    request.cls.log.info(f"For current box TSN {Settings.tsn} a valid person was found: {request.cls.person}")
                    break

    if not found:
        request.cls.log.error("Could not get any person. SKIP TEST.")
        pytest.skip("Could not get any person. SKIP TEST.")

    request.cls.log.info("")
    request.cls.log.info(":::::::::::: PRECONDITION END: Exit from setup_get_person() ::::::::::::")
