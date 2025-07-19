'''
Created on Jan 14, 2020

@author: mcretu
'''
from webportal.test_settings import WebPortalSettings as Settings
from webportal.client_api.search.assertions import SearchAssertions
from webportal.client_api.search.locators import SearchLocators
from webportal.client_api.guide.locators import GuideLocators
from webportal.client_api.guide.assertions import GuideAssertions
from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.manage.assertions import ManageAssertions
from webportal.client_api.my_shows.locators import MyShowsLocators
from webportal.client_api.my_shows.assertions import MyShowsAssertions
from webportal.client_api.what_to_watch.assertions import WhatToWatchAssertions
from webportal.client_api.ondemand.assertions import OnDemandAssertions
from hamcrest import *


class CablecoAssertions(SearchAssertions, GuideAssertions, ManageAssertions, MyShowsAssertions, WhatToWatchAssertions,
                        OnDemandAssertions):

    def __init__(self, obj):
        self.driver = obj.driver
        self.log = obj.log

    def verify_search_list_results(self, search_title):
        if self.driver.isElementDisplayedByXPath(SearchLocators.LOC_AUTO_SUGGEST_CABLECO_XPATH):
            found = False
            results = self.driver.getElementsByXPath(SearchLocators.LOC_SUGGESTED_LIST_TITLE_CABLECO_XPATH)
            for element in results:
                self.log.info(element.text)
                if search_title in element.text:
                    self.log.info(f"Check the title entered {search_title} in the auto suggested list {element.text}")
                    found = True
                    break
            assert found, "Searched Item is not Displayed in the results "
        else:
            assert False, "Search Results is not Displayed"

    def assert_LiveTv_Screen(self):
        self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_PLAYING_SHOW_CABLECO_CSS)
        self.assertElementPresentByCSS(GuideLocators.LOC_PLAYING_SHOW_CABLECO_CSS)

    def managePageSubMenus(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_MANAGE_PAGE_CSS)
        self.verify_manageToDoListPage()
        self.verify_manageOnePassManagerPage()

    def assert_KeepUntil_value_selected(self):
        self.assertElementPresentByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.assertLabelPresentByXpath('As long as possible', ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.log.info('The changed include value: "As long as possible" is correct')

    def assert_value_selected_OnePass(self):
        self.driver.waitUntilElementIsVisibleByXpath(ManageLocators.LOC_CONFIRM_NEW_KEEPUNTIL_VALUE_XPATH,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertLabelPresentByXpath('As long as possible', ManageLocators.LOC_CONFIRM_NEW_KEEPUNTIL_VALUE_XPATH)
        self.log.info("New Keep Until option: 'As long as possible' is changed")

    def assert_streaming_movies_folder_present(self):
        self.driver.refresh()
        self.driver.page_has_loaded()
        element = self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_STREAMING_CABLECO_MOVIES_CSS)
        if element is None:
            self.log.info("== As Expected: Folder 'Streaming Movies' is present. ==")
        else:
            self.log.error("== Folder 'Streaming Movies' was found. Should be deleted when it is empty. ==")
            assert_that(False, "== Folder 'Streaming Movies' was found. Should be deleted when it is empty. ==")
