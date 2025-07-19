from webportal.client_api.my_shows.locators import MyShowsLocators
from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.my_shows.labels import MyShowsLabels
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings as Settings
from hamcrest import *


class MyShowsAssertions(BaseAssertions):

    def assert_streaming_movies_folder_present(self):
        self.driver.refresh()
        self.driver.page_has_loaded()
        element = self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_STREAMING_MOVIES)
        if element is None:
            self.log.info("== As Expected: Folder 'Streaming Movies' is present. ==")
        else:
            self.log.error("== Folder 'Streaming Movies' was found. Should be deleted when it is empty. ==")
            assert_that(False, "== Folder 'Streaming Movies' was found. Should be deleted when it is empty. ==")

    def assert_shortcut_delete_show(self):
        self.assertElementPresentByCSS(MyShowsLocators.LOC_DELETE_SHOW)

    def my_show_message_assert(self):
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MY_SHOW_SIGN_IN_BUTTON_CSS)
        self.assertElementPresentByCSS(MyShowsLocators.LOC_MY_SHOW_SIGN_IN_BUTTON_CSS)
        self.assertElementPresentByXPATH(MyShowsLocators.LOC_MY_SHOW_WMD_XPATH)

    def verify_myShowsPage(self):
        self.driver.clickElementByCSS(MyShowsLocators.LOC_MY_SHOWS_TAB_CSS)
        self.driver.page_has_loaded()
        self.assertElementPresentByCSS(MyShowsLocators.LOC_MY_SHOWS_LIST)

    def assert_MyShows_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(MyShowsLocators.LOC_MY_SHOWS_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(MyShowsLocators.LOC_MY_SHOWS_HIGHLIGHTED_XPATH)
        self.log.info("My Shows menu item and is highlighted")

    def assert_Manage_submenu_hidden(self):
        self.assertElementNotPresentByXpath(ManageLocators.LOC_MANAGE_NAV_SUBMENU_XPATH)
        self.log.info("Manage submenu items are hidden")
