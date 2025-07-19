import pytest
from webportal.client_api.my_shows.assertions import MyShowsAssertions
from webportal.client_api.my_shows.page import MyShowsPage
from webportal.test_settings import WebPortalSettings as Settings
from webportal.factory.factory import Factory


@pytest.fixture(scope="function")
def setup_my_shows(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.my_shows_page = Factory.page_factory(request.cls)
    request.cls.my_shows_assertions = Factory.assertions_factory(request.cls)


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_delete_subscriptions(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_delete_subscriptions - method :::::::::::: \n")
    request.cls.api.delete_all_subscriptions()


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_delete_recordings(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_delete_recordings - method :::::::::::: \n")
    request.cls.api.delete_all_subscriptions()
    request.cls.api.delete_recordings_from_myshows()


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_delete_bookmarks(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_delete_bookmarks - method :::::::::::: \n")
    request.cls.service_api.delete_bookmarks(Settings.tsn)


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_create_onepass(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_create_onepass - method :::::::::::: \n")
    request.cls.api.one_pass_currently_airing_shows(1)


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_delete_everything(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_delete_everything - method :::::::::::: \n")
    request.cls.log.info("== Delete Recordings ==")
    request.cls.api.cancel_all_recordings()  # cancel and deletes all in-progress recordings
    request.cls.driver.pause(5)
    request.cls.api.empty_myshows_folder()  # deletes all the contents of the myshows folder.
    request.cls.api.delete_recordings_from_myshows()  # deletes content from folders from myshows folder
    request.cls.driver.pause(5)
    request.cls.log.info("== Delete OnePasses ==")
    request.cls.api.delete_all_subscriptions()
    request.cls.log.info("== Delete Bookmarks ==")
    request.cls.service_api.delete_bookmarks(Settings.tsn)
    request.cls.driver.pause(5)


@pytest.fixture(autouse=False, scope="function")
def setup_myshows_delete_all(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_myshows_delete_all - method :::::::::::: \n")
    request.cls.my_shows_page.select_button_sign_in()
    request.cls.my_shows_page.log_in()
    request.cls.my_shows_page.go_to_My_Shows()
    for i in range(5):
        request.cls.my_shows_page.delete_All_From_MyShows()
