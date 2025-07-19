from webportal.client_api.what_to_watch.locators import WhatToWatchLocators
from webportal.client_api.what_to_watch.labels import WhatToWatchLabels
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings as Settings


class WhatToWatchAssertions(BaseAssertions):

    def what_to_watch_onePassCreatedText_assert(self):
        self.assertTextPresent(WhatToWatchLabels.LBL_ONE_PASS_CREATED_TEXT)

    def what_to_watch_createOnePass_assert(self):
        self.mouseHover(WhatToWatchLocators.LOC_WTW_NEWLY_AVAILABLE_TILE_CSS)
        self.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_NEWLY_AVAILABLE_INFO_CSS)
        self.getElementText(WhatToWatchLocators.LOC_SHOWINFO_POPUP_EPISODENAME)

    def logo_assert(self):
        self.assertElementPresentByXPATH(WhatToWatchLocators.LOC_MSOBRANDING_IMAGE_XPATH)

    def searchBar_assert(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_SEARCH_CSS)

    def signInLink_assert(self):
        if Settings.mso.lower() == "cableco":
            self.log.info("This assertion is not valid for Cableco")
        if Settings.mso.lower() == "retail":
            element = self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_SIGN_IN_BUTTON_CSS)
            if element is None:
                self.log.error("'SignIn link' is NOT displayed")
                assert False, "'SignIn link' is NOT displayed"
            else:
                self.log.info("As Expected: 'SignIn link' is displayed")

    def signOutLink_NotPresent_assert(self):
        if Settings.mso.lower() == "cableco":
            self.log.info("This assertion is not valid for Cableco")
        if Settings.mso.lower() == "retail":
            self.assertElementNotPresentByLinkText(WhatToWatchLabels.LBL_SIGN_OUT)

    def mainDropDownMenu_NotPresent_assert(self):
        if Settings.mso.lower() == "cableco":
            self.log.info("This assertion is not valid for Cableco")
        if Settings.mso.lower() == "retail":
            self.driver.waitUntilElementIsNotVisibleByCSS(WhatToWatchLocators.LOC_MENU_ICON_MAIN_CSS)
            self.assertElementNotPresentByCSS(WhatToWatchLocators.LOC_MENU_ICON_MAIN_CSS)

    def help_assert(self):
        self.assertElementPresentByLinkText(WhatToWatchLabels.LBL_HELP)

    def mainPageTabs_assert(self):
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_WHAT_TO_WATCH_CSS, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByLinkText(WhatToWatchLabels.LBL_WHATTOWATCH)
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_MYSHOWS_CSS, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByLinkText(WhatToWatchLabels.LBL_MY_SHOWS)
        self.assertElementPresentByLinkText(WhatToWatchLabels.LBL_GUIDE_TEXT)
        self.assertElementPresentByLinkText(WhatToWatchLabels.LBL_MANAGE)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_SEARCH_CSS)

    def assert_Get_this_Show_displayed(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_GET_THIS_SHOW_WINDOW_CSS)
        self.log.info('Get this Show dialog is displayed')

    def assert_OnePass_Options_displayed(self):
        self.log.info('Verify if OnePass dialog is displayed')
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS)
        self.log.info('Create OnePass dialog is displayed')

    def assert_Modify_OnePass(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_MODIFY_ONEPASS_XPATH, Settings.HIGH_WAIT_TIME)
        self.assertElementVisibleByXpath(WhatToWatchLocators.LOC_MODIFY_ONEPASS_XPATH, "'Modify' button")

    def assert_Create_Whisper_OnePass(self):
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS)
        self.assertLabelPresentByCSS(WhatToWatchLabels.LBL_CREATE_ONEPASS_WHISPER,
                                     WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS)
        self.log.info('OnePass CREATE whisper is displayed and the text is correct')
        self.driver.waitUntilElementIsNotVisibleByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS,
                                                      Settings.HIGH_WAIT_TIME)

    def assert_Modify_displayed(self):
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS)

    def assert_Cancel_displayed(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS)
        self.log.info('Cancel option is displayed on the dialog')

    def assert_Cancel_Whisper_OnePass(self):
        self.log.info("Verify Cancel Whisper OnePass")
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS)
        self.assertLabelPresentByCSS(WhatToWatchLabels.LBL_CANCEL_ONEPASS_WHISPER,
                                     WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS)
        self.log.info('OnePass DELETE whisper is displayed and the text is correct')
        self.driver.waitUntilElementIsNotVisibleByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_WHISPER_CSS,
                                                      Settings.HIGH_WAIT_TIME)
        self.log.info("Verify 'Modify' is not visible anymore.")
        self.driver.waitUntilElementIsNotVisibleByCSS(WhatToWatchLocators.LOC_MODIFY_ONEPASS_XPATH, Settings.HIGH_WAIT_TIME)

    def assert_Remove_Modify_OnePass(self):
        self.log.info("Verify that 'Modify' button is not visible. (This means the asset doesn't have any OnePass)")
        self.driver.waitUntilElementIsNotVisibleByXpath(WhatToWatchLocators.LOC_MODIFY_ONEPASS_XPATH,
                                                        Settings.HIGH_WAIT_TIME)
        self.assertElementNotVisibleByXpath(WhatToWatchLocators.LOC_MODIFY_ONEPASS_XPATH)
        self.log.info('Modify button is not visible. This means the asset doesnt have any OnePass')

    def view_all_display(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_CONTENT_STRIP_XPATH,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXPATH(WhatToWatchLocators.LOC_WTW_CONTENT_STRIP_XPATH)

    def guest_user_logo_assert(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_LOGO_CSS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_LOGO_CSS)

    def box_selection_drop_down_assert(self):
        self.assertElementNotVisibleByXpath(WhatToWatchLocators.LOC_BOX_SELECTION_XPATH)

    def whatToWatchSubMenus(self):
        self.verify_onTvTodayPage()
        self.verify_sportsPage()
        self.verify_moviesPage()
        self.verify_tvSeriesPage()
        self.verify_kidsPage()
        self.verify_collectionsPage()
        self.verify_boxSetsPage()
        self.verify_justForMePage()

    def verify_onTvTodayPage(self):
        self.log.info("I'm in verify_onTvTodayPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_WTW_ON_TV_TODAY)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_ON_TV_TODAY_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_ON_TV_TODAY_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_ON_TV_TODAY_STRIPS)
        self.driver.page_has_loaded()
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_sportsPage(self):
        self.log.info("I'm in verify_sportsPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_SPORTS)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_SPORTS_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_SPORTS_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_SPORTS_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_moviesPage(self):
        self.log.info("I'm in verify_moviesPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_MOVIES)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_MOVIES_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_MOVIES_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_MOVIES_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_tvSeriesPage(self):
        self.log.info("I'm in verify_tvSeriesPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_TV_SERIES)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_TV_SERIES_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_TV_SERIES_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_TV_SERIES_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_kidsPage(self):
        self.log.info("I'm in verify_kidsPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_KIDS)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_KIDS_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_KIDS_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_KIDS_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_collectionsPage(self):
        self.log.info("I'm in verify_collectionsPage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_COLLECTIONS)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_COLLECTIONS_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_COLLECTIONS_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_COLLECTIONS_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_boxSetsPage(self):
        self.log.info("I'm in verify_boxSetsPage method.")
        try:
            self.driver.clickElementByCSS(WhatToWatchLocators.LOC_BOX_SETS)
            self.driver.page_has_loaded(5)
            self.assertElementPresentByXpath(WhatToWatchLocators.LOC_BOX_SETS_ACTIVE)
            self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_BOX_SETS_STRIPS,
                                                           Settings.HIGH_WAIT_TIME)
            self.assertElementPresentByXpath(WhatToWatchLocators.LOC_BOX_SETS_STRIPS)
            self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
            self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
            self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)
        except Exception:
            self.log.info("Box sets submenu is not available in WTW category")
            pass

    def verify_justForMePage(self):
        self.log.info("I'm in verify_justForMePage method.")
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_JUST_FOR_ME)
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_JUS_FOR_ME_ACTIVE)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_JUST_FOR_ME_STRIPS,
                                                       Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_JUST_FOR_ME_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_STRIP)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_FEED)

    def verify_ViewAllOfaStrip(self):
        self.log.info("I'm in verify_ViewAllOfaStrip method.")
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_VIEW_ALL_XPATH)
        self.driver.page_has_loaded(5)
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_VIEW_ALL_ITEMS, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_VIEW_ALL_ITEMS)

    def assert_OnTVToday(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_ON_TV_TODAY_STRIP_NAME_XPATH)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_ON_TV_TODAY_STRIP_NAME_XPATH)

    def assert_WTW_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_HIGHLIGHTED_XPATH)
        self.log.info("What to Watch menu item and is highlighted")

    def assert_JustForMe_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_JUST_FOR_ME_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_JUST_FOR_ME_HIGHLIGHTED_XPATH)
        self.log.info("Just For Me menu item and is highlighted")

    def assert_WTW_not_highlighted(self):
        self.driver.waitUntilElementIsNotVisibleByXpath(WhatToWatchLocators.LOC_WTW_HIGHLIGHTED_XPATH)
        self.assertElementNotPresentByXpath(WhatToWatchLocators.LOC_WTW_HIGHLIGHTED_XPATH)
        self.log.info("What to Watch menu item and is not highlighted")

    def assert_Menu_displayed(self):
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_NAV_MENU_XPATH)
        self.log.info("The menu is successfully displayed")

    def assert_WTW_submenu_hidden(self):
        self.assertElementNotPresentByXpath(WhatToWatchLocators.LOC_WTW_NAV_SUBMENU_XPATH)
        self.log.info("What to Watch submenu items are hidden")

    def assert_Info_card_displayed(self):
        self.driver.waitUntilElementIsDisplayedByCSS(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_CSS)
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_CSS)
        self.log.info("Info card is displayed")

    def assert_ShareFormat(self):
        self.assertLabelPresentByXpath('Share this show', WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TITLE_XPATH)
        self.log.info("Share this show title is displayed")
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_FACEBOOK_XPATH)
        self.log.info("Facebook icon is displayed")
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TWITTER_XPATH)
        self.log.info("Twitter icon is displayed")
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_EMAIL_XPATH)
        self.log.info("Email icon is displayed")

    def assert_Share_displayed(self):
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TITLE_XPATH)
        self.log.info("Share pop up window is displayed")

    def assert_Facebook_share_format(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_FACEBOOK_CSS)
        self.log.info("Facebook URL is correct")

    def assert_Facebook_displayed(self):
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHARE_FACEBOOK_PAGE_XPATH)
        self.log.info("Facebook window is displayed")

    def assert_Twitter_share_format(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TWITTER_CSS)
        self.log.info("Twitter URL is correct")

    def assert_Twitter_displayed(self):
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHARE_TWITTER_PAGE_XPATH)
        self.log.info("Twitter window is displayed")

    def assert_Email_share_format(self):
        self.assertElementPresentByCSS(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_EMAIL_URL_CSS)
        self.log.info("Email URL is correct")

    def assert_Email_displayed(self):
        self.assertElementPresentByXpath(WhatToWatchLocators.LOC_WTW_SHARE_EMAIL_PAGE_XPATH)
        self.log.info("Email window is displayed")
