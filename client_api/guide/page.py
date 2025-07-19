from webportal.client_api.guide.locators import GuideLocators
from webportal.client_api.guide.labels import GuideLabels
from webportal.client_api.base.page import BasePage
from webportal.test_settings import WebPortalSettings as Settings


class GuidePage(BasePage):

    def go_to_Guide(self):
        self.log.info("Going to Guide...")
        if Settings.mso.lower() == "cableco":
            self.driver.waitUntilElementIsDisplayedByLINK_TEXT(GuideLocators.LOC_GUIDE_LINK_TEXT, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByLinkText(GuideLocators.LOC_GUIDE_LINK_TEXT)
            if self.driver.isElementDisplayedByCSS(GuideLocators.LOC_GUIDE_OK_CSS):
                self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_OK_CSS)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_FILTER_CSS, Settings.HIGH_WAIT_TIME)
        if Settings.mso.lower() == "retail":
            self.driver.waitUntilElementIsDisplayedByLINK_TEXT(GuideLocators.LOC_GUIDE_LINK_TEXT, Settings.HIGH_WAIT_TIME)
            self.driver.clickElementByLinkText(GuideLocators.LOC_GUIDE_LINK_TEXT)
            self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_GUIDE_FILTER_CSS, Settings.HIGH_WAIT_TIME)

    def enter_text_in_form(self):
        self.driver.search(GuideLabels.LBL_TIVO, GuideLocators.LOC_GOOGLE_FORM_CSS)

    def Nav_to_an_airing_show_from_Guide(self):
        """
        Navigates to Guide page
        :return: channel having an airing show (Play icon and Live TV icon present over the preview poster)
        """
        self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_GRID_CSS)
        self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_FILTER_CSS)
        self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_ALLCHANNELS_XPATH)
        self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_NOW_CSS)
        return self.select_an_airing_channel(channels=None)

    def Nav_And_Select_Live_Tv_From_Guide(self):
        """
        Navigates to Guide page and select a live show
        :return: nothing
        """
        self.go_to_Guide()
        airing_channel = self.Nav_to_an_airing_show_from_Guide()
        if airing_channel is not None:
            airing_channel.click()
        else:
            self.log.error("Cannot found child element, cannot click on it.")
            assert False, "Cannot found child element, cannot click on it."

    def Select_Live_Tv_Button(self):
        self.log.info("I'm in Select_Live_Tv_Button() method.")
        element = self.driver.clickElementByCSS(GuideLocators.LOC_GUIDEWATCH_CSS)
        if element is None:
            self.log.info("There must be more sources to choose from. Lets look for the pop-up 'Watch Now' first.")
            watchnow_popup = self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_PLAYING_SHOW_POPUP_TITLE)
            if watchnow_popup is None:
                self.log.warning("Popup 'Watch Now' having stream sources options (live TV, Prime Video, "
                                 "Prime Membership, etc) was not detected...")
            else:
                self.log.info("'Watch Now' popup displayed. Lets select 'LIVE TV' from it.")
                self.driver.clickElementByCSS(GuideLocators.LOC_PLAYING_SHOW_FROM_POPUP_CSS)

    def Get_this_Show_From_Guide(self):
        self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_GRID_CSS)
        self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_NOW_CSS)

    def Schedule_Record_from_Guide(self, channels):
        self.log.info("I'm in Schedule_Record_from_Guide() method.")
        airing_channel = self.select_an_airing_channel(channels)

        if airing_channel is not None:
            try:
                self.driver.clickElementByCSS(GuideLocators.LOC_GET_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
                found = self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_RECORD_THIS_EPISODE_BUTTON_CSS)
                if found is None:
                    self.driver.clickElementByCSS(GuideLocators.LOC_RECORD_THIS_SHOW_BUTTON_CSS)
                else:
                    self.driver.clickElementByCSS(GuideLocators.LOC_RECORD_THIS_EPISODE_BUTTON_CSS)
                self.driver.clickElementByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
                recorded_asset = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS)
                recorded_asset_1 = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS_1)
                return recorded_asset, recorded_asset_1
            except Exception:
                try:
                    self.driver.clickElementByCSS(GuideLocators.LOC_RECORD_THIS_SHOW_BUTTON_CSS)
                    self.driver.waitUntilElementIsClickableByCSS(
                        GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
                    self.driver.clickElementByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
                    recorded_asset = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS)
                    recorded_asset_1 = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS_1)
                    return recorded_asset, recorded_asset_1
                except Exception:
                    pass
        else:
            self.log.info("Checked for multiple shows in the guide and Found none of them are currently Airing now")

    def select_an_airing_channel(self, channels):
        self.log.info("I'm in select_an_airing_channel() method.")
        if channels is None:
            elements = self.driver.waitUntilElementsAreVisibleByCSS(GuideLocators.LOC_CHANNEL_LIST_UNLOCKED)
            if elements is not None:
                channel_list = []
                for item in elements:
                    channel_number = item.get_attribute(GuideLocators.LOC_GUIDE_CHANNEL_NUMBER)
                    self.log.info(f"Found channel nr.: {channel_number}")
                    channel_list.append(channel_number)
        else:
            channel_list = channels
        # try to find an airing channel
        airing_channel = None
        live_tv = None
        counter = 0
        self.log.info("Looking for an airing channel...")
        while airing_channel is None and live_tv is None and counter < len(channel_list):
            self.log.info(f"Try channel nr.: {channel_list[counter]}")
            parent = self.driver.waitUntilElementIsClickableByCSS(
                f"[{GuideLocators.LOC_GUIDE_CHANNEL_NUMBER}='{channel_list[counter]}']")
            child = parent.find_element_by_css_selector("[class='show-description ellipses-truncated-text']")
            if child is not None:
                child.click()
                self.log.info(f"Successfully selected channel: {channel_list[counter]}")
            else:
                assert False, self.log.info(f"Could not select channel: {channel_list[counter]}")
            self.log.info("Check that current channel have Play icon and Live TV icon. If not, try another channel...")
            airing_channel = self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_AIRING_NOW_CSS)
            live_tv = self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDEWATCH_CSS)
            counter = counter + 1
        return airing_channel

    def Nav_My_Show_and_select_asset(self, recorded_asset, recorded_asset_1):
        self.log.info("I'm in Nav_My_Show_and_select_asset() method.")
        self.driver.clickElementByCSS(GuideLocators.LOC_MY_SHOWS_TAB_CSS)
        self.driver.refresh()  # refresh is needed because the Modify button may not be displayed after scheduling a rec
        self.log.info("=== Select the show by title ===")
        element1 = self.driver.waitUntilElementIsClickableByXpath(".//*[@title='" + recorded_asset + "']")
        if element1 is not None:
            self.driver.clickElementByXPATH(".//*[@title='" + recorded_asset + "']")
            self.log.info("Show successfully selected.")
        else:
            self.log.info("=== Select the show by title having apostrophe(') ===")
            element2 = self.driver.waitUntilElementIsClickableByXpath(".//*[@title=\"" + recorded_asset + "\"]")
            if element2 is not None:
                self.driver.clickElementByXPATH(".//*[@title=\"" + recorded_asset + "\"]")
                self.log.info("Show successfully selected.")
            else:
                self.log.info("=== Select the title having long text ===")
                element3 = self.driver.waitUntilElementIsClickableByXpath(".//*[@title='" + recorded_asset_1 + "']")
                if element3 is not None:
                    self.driver.clickElementByXPATH(".//*[@title='" + recorded_asset_1 + "']")
                    self.log.info("Show successfully selected.")
                else:
                    self.log.error("Could not select the show.")
                    raise Exception("Could not select the show.")
        notification = self.driver.waitUntilElementIsVisibleByCSS(GuideLocators.LOC_NOTIFICATION_MSG_CSS)
        if notification is not None:
            self.log.info(f"== {notification.text} ==\n")
        # TO UNCOMMENT WHEN NDVR is IMPLEMENTED
        # self.log.info("Click on icon Play displayed over the poster image")
        # self.driver.clickElementByCSS(GuideLocators.LOC_WATCHNOW_CSS)
        # self.log.info("Click on 'My Recording' in the displayed popup 'Watch Now'")
        # self.driver.clickElementByXPATH(GuideLocators.LOC_MY_RECORDING_XPATH)

    def close_player_screen(self):
        self.driver.clickElementByXPATH(GuideLocators.CLOSE_WINDOW_SCREEN_XPATH)
        self.driver.waitUntilElementIsNotVisibleByCSS(GuideLocators.CLOSE_WINDOW_SCREEN_XPATH)

    def nav_to_guide_select_a_show(self):
        if Settings.mso.lower() == "cableco":
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_TAB_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_TAB_CSS)
            if self.driver.isElementDisplayedByCSS(GuideLocators.LOC_GUIDE_OK_CSS):
                self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_OK_CSS)
        if Settings.mso.lower() == "retail":
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_TAB_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_TAB_CSS)
        self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_FILTER_CSS)
        self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_FILTER_CSS)
        self.driver.waitUntilElementIsClickableByXpath(GuideLocators.LOC_GUIDE_ALLCHANNELS_XPATH)
        self.driver.clickElementByXPATH(GuideLocators.LOC_GUIDE_ALLCHANNELS_XPATH)
        self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GUIDE_NOW_CSS)
        self.driver.clickElementByCSS(GuideLocators.LOC_GUIDE_NOW_CSS)
        self.driver.waitUntilElementIsClickableByXpath(GuideLocators.LOC_ELEMENT_IN_GUIDE_BY_XPATH)
        self.driver.clickElementByXPATH(GuideLocators.LOC_ELEMENT_IN_GUIDE_BY_XPATH)
        self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_GET_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
        self.driver.clickElementByCSS(GuideLocators.LOC_GET_THIS_SHOW_OR_EPISODE_BUTTON_CSS)

    def schedule_record_from_guide_and_get_the_element(self):
        try:
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_RECORD_THIS_EPISODE_BUTTON_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_RECORD_THIS_EPISODE_BUTTON_CSS)
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
            element_visible = self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_RECORD_WHISPER_CSS)
            recorded_asset = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS)
            recorded_episode_name = self.driver.getElementTextByCSS(GuideLocators.LOC_EPISODE_NAME_CSS)
            episode_number = self.driver.getElementTextByCSS(GuideLocators.LOC_EPISODE_NUMBER_CSS)
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_MY_SHOWS_TAB_CSS)
        except Exception:
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_RECORD_THIS_SHOW_BUTTON_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_RECORD_THIS_SHOW_BUTTON_CSS)
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
            self.driver.clickElementByCSS(GuideLocators.LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS)
            element_visible = self.driver.waitUntilElementIsDisplayedByCSS(GuideLocators.LOC_RECORD_WHISPER_CSS)
            recorded_asset = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS)
            recorded_episode_name = self.driver.getElementTextByCSS(GuideLocators.LOC_EPISODE_NAME_CSS)
            episode_number = self.driver.getElementTextByCSS(GuideLocators.LOC_EPISODE_NUMBER_CSS)
            self.driver.waitUntilElementIsClickableByCSS(GuideLocators.LOC_MY_SHOWS_TAB_CSS)
        recorded_big_asset = self.driver.getElementTextByCSS(GuideLocators.LOC_RECORDED_ASSET_CSS_1)
        return recorded_asset, recorded_episode_name, episode_number, recorded_big_asset, element_visible
