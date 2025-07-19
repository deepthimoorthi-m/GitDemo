from webportal.client_api.search.locators import SearchLocators
from webportal.client_api.search.labels import SearchLabels
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings
import re


class SearchAssertions(BaseAssertions):

    def get_search_results(self, search_title):
        self.log.info("I'm in get_search_results() method.")
        self.driver.page_has_loaded(5)
        search_results = self.driver.waitUntilElementIsClickableByCSS(SearchLocators.LOC_SUGGESTED_LIST_TITLE_CSS)
        if search_results is None:
            self.log.error(f"No suggestions available for searched text '{search_title}'")
            assert False, f"No suggestions available for searched text '{search_title}'"
        items = search_results.find_elements_by_tag_name("li")
        self.log.info(f"Items suggested for the searched text '{search_title}' are:")
        for element in items:
            if element.text is not None:
                self.log.info(element.text)
        return items

    def verify_search_list_results(self, search_title):
        items = self.get_search_results(search_title)
        self.verify_search_item_name(search_title, items)

    def verify_search_asset_name(self):
        self.assertLabelPresentByXpath(SearchLabels.LBL_SEARCH_EP_SHOWS,
                                       SearchLocators.LOC_SUGGESTED_LIST_SHOW_XPATH)
        self.log.info(f"Asset name: {SearchLabels.LBL_SEARCH_EP_SHOWS} is displayed in the asset details")

    def verify_search_item_format(self, **kwargs):
        self.log.info("I'm in verify_search_item_format() method.")

        search_year_from_mind = kwargs.get('year', None)
        search_title_from_mind = kwargs.get('title', None)
        type_title = kwargs.get('type_title', None)

        suggested_items = self.get_search_results(search_title_from_mind)
        if type_title == 'person':
            search_title_from_ui = self.verify_search_item_name(search_title_from_mind, suggested_items, True)
        else:
            search_title_from_ui = self.verify_search_item_name(search_title_from_mind, suggested_items)
        self.log.info(f"Check the format {type_title} for {search_title_from_mind} in "
                      f"the auto suggested list {search_title_from_ui.text}")
        if type_title == "episode":
            self.verify_search_episode_name()
            self.verify_search_poster(type_title, suggested_items)
            self.verify_search_year()
            self.verify_search_genre()
            self.verify_search_rating()
        elif type_title == "movie":
            self.verify_search_year(search_year_from_mind=search_year_from_mind)
        elif type_title == "person":
            self.verify_search_person_name(search_title_from_mind)
            self.verify_search_poster(type_title, suggested_items)
            self.verify_search_person_roles()
        elif type_title == "series":
            self.verify_search_poster(type_title, suggested_items)
            self.verify_search_genre()
            self.verify_search_rating()
        elif type_title == "sport_team":
            self.verify_search_sport_team_name(SearchLabels.LBL_SEARCH_SPORT_TEAM)
            self.verify_search_poster(type_title, suggested_items)

    def verify_search_item_name(self, search_title_from_mind, items, strict_compare=False):
        self.log.info("I'm in verify_search_item_name() method.")
        found = False
        self.log.info(f"Check the title entered {search_title_from_mind} in the auto suggested list...")
        for element in items:
            if strict_compare:
                self.log.info("Strict comparison.")
                search_title_from_ui = element.text.split("\n")
                self.log.info(f"=== Extracted '{search_title_from_ui[0]}' from text '{element.text}' ===")
                if search_title_from_mind == search_title_from_ui[0]:
                    self.log.info(f"Searched text '{search_title_from_mind}' found in the auto-suggested list."
                                  f" Matched with element '{element.text}'")
                    found = True
                    break
            else:
                if search_title_from_mind in element.text:
                    self.log.info(f"Searched text '{search_title_from_mind}' found in the auto-suggested list."
                                  f" Matched with element '{element.text}'")
                    found = True
                    break
        if not found:
            self.log.error(f"Searched text '{search_title_from_mind}' was NOT found in the auto-suggested list.")
        assert found, f"Searched text '{search_title_from_mind}' was NOT found in the auto-suggested list."
        return element

    def verify_search_person_name(self, search_item):
        self.log.info("I'm in verify_search_person_name() method.")
        self.assertLabelPresentByXpath(search_item, SearchLocators.LOC_SUGGESTED_LIST_PERSON_NAME_XPATH)
        self.log.info(f"Person name: {search_item} is displayed in the item details")

    def verify_search_sport_team_name(self, search_item):
        self.assertLabelPresentByXpath(search_item, SearchLocators.LOC_SUGGESTED_LIST_SPORT_XPATH)
        self.log.info(f"Sport team name: {search_item} is displayed in the item details")

    def verify_search_person_roles(self):
        self.log.info("I'm in verify_search_person_roles() method.")
        found_person_roles = self.driver.waitUntilElementIsDisplayedByCSS(SearchLocators.LOC_SUGGESTED_LIST_ROLES_CSS)
        if found_person_roles is None:
            self.log.error("Person Roles is NOT displayed in the asset details.")
            raise Exception("Person Roles is NOT displayed in the asset details.")
        self.log.info(f"Person Roles '{found_person_roles.text}' is displayed in the asset details")

    def verify_search_episode_name(self):
        """
        Not all results have the episode name displayed in the first matched item,
        therefore look into the next suggested items to check that this feature is implemented
        """
        self.log.info("I'm in verify_search_episode_name() method.")
        sle = SearchLocators.LOC_SUGGESTED_LIST_EPISODE_NAME_XPATH
        found_episodes_name = self.driver.waitUntilElementsArePresentByXpath(sle)
        if found_episodes_name is None:
            self.log.error("Episode Name is NOT displayed in search suggested list.")
            raise Exception("Episode Name is NOT displayed in search suggested list.")
        self.log.info("Episode Name is displayed in the asset details, ie:")
        for name in found_episodes_name:
            self.log.info(getattr(name, 'text', '== NO EPISODE NAME AVAILABLE =='))

    def verify_search_poster(self, search_type, suggested_list_ui):
        self.log.info(f"I'm in verify_search_poster({search_type}) method.")
        if search_type == "episode" or search_type == "movie":
            self.assertElementPresentByXpath(SearchLocators.LOC_SUGGESTED_LIST_POSTER_XPATH)
        if search_type == "person":
            found = False
            for suggested_item in suggested_list_ui:
                slp = SearchLocators.LOC_SUGGESTED_LIST_PERSON_POSTER_CSS
                found_poster = self.driver.getElementFromParentByCSS(suggested_item, slp)
                if found_poster is not None:
                    found = True
                    break
            if found is False:
                self.log.error("Person Roles is NOT displayed in the asset details.")
                raise Exception("Person Roles is NOT displayed in the asset details.")
        self.log.info("Poster is displayed in the asset details")

    def verify_search_year(self, **kwargs):
        """
        Not all results have the year displayed in the first matched item,
        therefore look into the next suggested items to check that this feature is implemented
        """
        self.log.info("I'm in verify_search_year() method.")
        search_year_from_mind = kwargs.get('search_year_from_mind', None)
        found_year_list = self.driver.waitUntilElementsArePresentByXpath(SearchLocators.LOC_SUGGESTED_LIST_YEAR_XPATH)
        if found_year_list is None:
            self.log.error("Year is NOT displayed in search suggested list.")
            raise Exception("Year is NOT displayed in search suggested list.")
        self.log.info("Year is displayed in the asset details, ie:")
        year_suggested_list = []
        for year in found_year_list:
            year_suggested = getattr(year, 'text', '== NO YEAR AVAILABLE ==')
            self.log.info(year_suggested)
            year_suggested_list.append(year_suggested)
        if search_year_from_mind is not None:
            self.log.info(f"Movie Year was provided from mind: {search_year_from_mind}. Perform validation.")
            if f"({search_year_from_mind})" not in year_suggested_list:
                self.log.error("No valid movie suggestion was provided. Year of the movie was not found in suggested list.")
                raise Exception("No valid movie suggestion was provided. Year of the movie was not found in suggested list.")
            self.log.info(f"Movie Year provided from mind {search_year_from_mind} was found listed in suggestions.")

    def verify_search_rating(self):
        self.log.info("I'm in verify_search_rating() method.")
        found_rating = self.driver.getElementTextByXpath(SearchLocators.LOC_SUGGESTED_LIST_RATING_XPATH)
        if found_rating is None:
            self.log.error("Rating is NOT displayed in the asset details.")
            raise Exception("Rating is NOT displayed in the asset details.")
        self.log.info(f"Rating '{found_rating}' is displayed in the asset details.")

    def verify_search_genre(self):
        self.log.info("I'm in verify_search_genre() method.")
        found_genre = self.driver.getElementTextByXpath(SearchLocators.LOC_SUGGESTED_LIST_GENRE_XPATH)
        if found_genre is None:
            self.log.error("Genre is NOT displayed in the asset details.")
            raise Exception("Genre is NOT displayed in the asset details.")
        self.log.info(f"Genre '{found_genre}' is displayed in the asset details.")

    def search_menu_assert(self):
        self.driver.waitUntilElementIsDisplayedByCSS(SearchLocators.LOC_SEARCH_CSS)
        self.assertElementPresentByCSS(SearchLocators.LOC_SEARCH_CSS)

    def search_field_not_present_assert(self):
        self.assertElementNotPresentByCSS(SearchLocators.LOC_AUTO_SEARCH_LIST_CSS)

    def verify_search_results_person(self, search_title):
        if self.driver.isElementDisplayedByXPath(SearchLocators.LOC_AUTO_SUGGEST_XPATH):
            found = False
            results = self.driver.waitUntilElementsAreVisibleByCSS(SearchLocators.LOC_SUGGESTED_LIST_PERSON_CSS)
            for element in results:
                self.log.info(f"Check the title entered {search_title} in the auto suggested list '{element.text}'")
                if search_title in element.text:
                    found = True
            assert found, f"Searched Item '{search_title}' is not Displayed in the auto suggested list '{element.text}'"
        else:
            assert False, "Search Results is not Displayed"
