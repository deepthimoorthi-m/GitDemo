from webportal.client_api.what_to_watch.locators import WhatToWatchLocators
from webportal.client_api.what_to_watch.labels import WhatToWatchLabels
from webportal.client_api.base.page import BasePage
from webportal.test_settings import WebPortalSettings as Settings


class WhatToWatchPage(BasePage):

    def go_to_What_to_Watch(self):
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_WHAT_TO_WATCH_CSS)
        self.driver.clickElementByLinkText(WhatToWatchLabels.LBL_WHATTOWATCH)

    def select_Get_this_Show(self):
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_WTW_GET_THIS_SHOW_BUTTON_CSS)
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_WTW_GET_THIS_SHOW_BUTTON_CSS)

    def select_create_OnePass_option(self):
        self.driver.waitUntilElementIsClickableByCSS(WhatToWatchLocators.LOC_WTW_ONEPASS_EDIT_WINDOW_CSS)
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_OPTION_CSS)

    def select_create_OnePass_button(self):
        self.driver.clickElementByCSS(WhatToWatchLocators.LOC_CREATE_ONEPASS_BUTTON_CSS)

    def select_share(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_XPATH)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_XPATH)

    def select_Facebook(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_FACEBOOK_XPATH)
        self.driver.switch_window(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_FACEBOOK_XPATH)

    def select_Twitter(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TWITTER_XPATH)
        self.driver.switch_window(WhatToWatchLocators.LOC_WTW_SHOW_SHARE_TWITTER_XPATH)

    def select_Cancel(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_CANCEL_ONEPASS_OPTION_XPATH)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_CANCEL_ONEPASS_OPTION_XPATH)

    def confirm_Cancel(self):
        self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_CANCEL_ONEPASS_CONFIRM_XPATH)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_CANCEL_ONEPASS_CONFIRM_XPATH)

    def asset_with_OnePass(self):
        return self.driver.getElementTextByXpath(WhatToWatchLocators.LOC_ASSET_NAME_XPATH),\
            self.driver.getElementTextByCSS(WhatToWatchLocators.LOC_ASSET_SEASON_EPISODE_CSS),\
            self.driver.getElementTextByXpath(WhatToWatchLocators.LOC_ASSET_EPISODE_NAME_XPATH)

    def feature_content(self):
        try:
            self.driver.page_has_loaded()
            self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_WTW_VIEW_ALL_XPATH,
                                                           Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_VIEW_ALL_XPATH)
        except Exception:
            self.driver.refresh()
            self.driver.page_has_loaded()
            self.driver.waitUntilElementIsClickableByXpath(WhatToWatchLocators.LOC_WTW_VIEW_ALL_XPATH,
                                                           Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_VIEW_ALL_XPATH)

    def poster_content(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_POSTER_CONTENT_XPATH,
                                                       Settings.HIGH_WAIT_TIME)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_POSTER_CONTENT_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_SIGN_IN_GTS_XPATH,
                                                       Settings.HIGH_WAIT_TIME)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_SIGN_IN_GTS_XPATH)

    def select_an_asset(self):
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_ON_TV_TODAY_ASSET_XPATH)
        self.driver.clickElementByXPATH(WhatToWatchLocators.LOC_WTW_ON_TV_TODAY_ASSET_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(WhatToWatchLocators.LOC_WTW_ON_TV_TODAY_ASSET_XPATH)
