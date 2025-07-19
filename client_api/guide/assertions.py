from webportal.client_api.guide.locators import GuideLocators
from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings as Settings


class GuideAssertions(BaseAssertions):

    def assertGoogleLogoPresent(self):
        self.assertElementPresentByXPATH(GuideLocators.LOC_GOOGLE_LOGO)

    def assertLiveTV(self):
        self.assertElementPresentByCSS(GuideLocators.LOC_RECORDING_ICON)

    def assert_LiveTv_Screen(self):
        self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_PLAYING_SHOW_CSS)
        self.assertElementPresentByCSS(GuideLocators.LOC_PLAYING_SHOW_CSS)

    def guide_page(self):
        if Settings.mso.lower() == "cableco":
            self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDE_XPATH, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_XPATH)
            self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_OK_CSS)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_GRID_CELL_CSS, Settings.HIGH_WAIT_TIME)
            self.assertElementPresentByCSS(GuideLocators.LOC_GUIDE_GRID_CELL_CSS)
        if Settings.mso.lower() == "retail":
            self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDE_XPATH, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_XPATH)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_GRID_CELL_CSS, Settings.HIGH_WAIT_TIME)
            self.assertElementPresentByCSS(GuideLocators.LOC_GUIDE_GRID_CELL_CSS)

    def assert_poster_present(self):
        self.log.info("I'm in assert_poster_present() method. Guest User Experience.")
        self.driver.clickElementByXPATH(GuideLocators.LOC_SHOWS_POSTER_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GTS_BUTTON)
        self.log.info("Check for 'Sign In to Get This Show' button to be displayed")
        self.assertElementPresentByXPATH(GuideLocators.LOC_GTS_BUTTON)

    def assert_LiveTv_Button(self):
        self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDEWATCH_XPATH, Settings.LOW_WAIT_TIME)
        self.assertElementPresentByXPATH(GuideLocators.LOC_GUIDEWATCH_XPATH)

    def verifyGuidePage(self):
        if Settings.mso.lower() == "cableco":
            self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDE_XPATH, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_XPATH)
            if self.driver.isElementDisplayedByCSS(GuideLocators.LOC_GUIDE_OK_CSS):
                self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_OK_CSS)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_LIST_CSS)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_CONTENT)
            self.assertElementPresentByCSS(GuideLocators.LOC_GUIDE_LIST_CSS)
        if Settings.mso.lower() == "retail":
            self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDE_XPATH, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_XPATH)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_LIST_CSS)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_CONTENT)
            self.assertElementPresentByCSS(GuideLocators.LOC_GUIDE_LIST_CSS)

    def assert_my_recording_Screen(self):
        self.assertElementPresentByCSS(GuideLocators.LOC_RECORDED_PLAYER_SCREEN_CSS)

    def assert_verify_recorded_element(self):
        self.driver.waitUntilElementIsVisibleByCSS(GuideLocators.LOC_RECORDED_WHISPER_CSS)
        self.assertElementPresentByCSS(GuideLocators.LOC_RECORDED_WHISPER_CSS)

    def assert_Recording_icon_present(self):
        try:
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_RECORD_ICON_CSS)
            self.assertElementPresentByCSS(GuideLocators.LOC_RECORD_ICON_CSS)
        except Exception:
            self.assertElementPresentByCSS(GuideLocators.LOC_RECORD_ICON_FROM_TITLE_CSS)

    def assert_LiveTv_Screen_Not_Present(self):
        self.assertElementNotPresentByCSS(GuideLocators.LOC_RECORDED_PLAYER_SCREEN_CSS)

    def assert_Guide_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(GuideLocators.LOC_GUIDE_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(GuideLocators.LOC_GUIDE_HIGHLIGHTED_XPATH)
        self.log.info("Guide menu item is highlighted")

    def assert_Manage_submenu_hidden(self):
        self.assertElementNotPresentByXpath(ManageLocators.LOC_MANAGE_NAV_SUBMENU_XPATH)
        self.log.info("Manage submenu items are hidden")

    def verify_recorded_whisper(self, element_visible):
        if element_visible is not None:
            self.log.info("Recording Whisper Appeared")
        else:
            assert False, "Recording Whisper Did NOT Appeared"
