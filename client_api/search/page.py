from webportal.client_api.search.locators import SearchLocators
from webportal.client_api.base.page import BasePage
import re


class SearchPage(BasePage):

    def text_search_field(self, search_title):
        self.driver.clickElementByCSS(SearchLocators.LOC_SEARCH_CSS)
        self.enter_search_text(search_title)

    def enter_search_text(self, search_title):
        self.driver.waitUntilElementIsClickableByXpath(SearchLocators.LOC_TEXT_FIELD_XPATH)
        self.driver.typeTextByXPath(search_title, SearchLocators.LOC_TEXT_FIELD_XPATH)
        self.driver.page_has_loaded()
        self.driver.waitUntilElementIsClickableByXpath(SearchLocators.LOC_AUTO_SUGGEST_XPATH)

    def delete_search_text_from_field(self):
        self.driver.clearSearchTextFieldByXpath(SearchLocators.LOC_TEXT_FIELD_XPATH)

    def close_search_field(self):
        self.driver.closeWindowActionByCSS(SearchLocators.LOC_CLOSE_BUTTON_CSS)
        self.driver.waitUntilElementIsNotVisibleByCSS(SearchLocators.LOC_CLOSE_BUTTON_CSS)

    def open_in_search(self, item):
        self.driver.page_has_loaded()
        search_results = self.driver.waitUntilElementIsClickableByCSS(SearchLocators.LOC_SUGGESTED_LIST_TITLE_CSS)
        items = search_results.find_elements_by_tag_name("li")
        self.log.info(f"Items suggested for the searched text '{item}' are:")
        self.driver.clickElementByLinkText(items[0].text)
        self.driver.page_has_loaded(15)

    def find_episode_title(self):
        search_results = self.driver.waitUntilElementIsVisibleByXpath(SearchLocators.LOC_ALL_EPISODES_STRIP_XPATH)
        items = search_results.find_elements_by_tag_name("li")
        for episode in items:
            episode_name = episode.text
            self.log.info(f"Episode found: {episode_name}")
            if episode_name.count("\'") >= 2:
                value = re.search(r"\'(.*?)\'", episode_name).group(0)[1:-1]
                self.log.info(f"The Episode found {value}")
                return value
