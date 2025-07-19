from webportal.client_api.ondemand.locators import OnDemandLocators
from webportal.client_api.ondemand.labels import OnDemandLabels
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings as Settings
import re


class OnDemandAssertions(BaseAssertions):

    def assert_on_demand_menu(self):
        self.assertElementPresentByCSS(OnDemandLocators.LOC_MY_RENTALS_CSS)

    def assert_all_titles(self):
        self.driver.waitUntilElementIsDisplayedByCSS(OnDemandLocators.LOC_ALL_TITLES_CSS)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_ON_DEMAND_GRID_CSS)

    def assert_pop_up(self, movie, text):
        pop_up = self.driver.waitUntilElementIsDisplayedByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)
        verify_text = pop_up.find_element_by_css_selector(".ui-dialog-titlebar")
        if OnDemandLabels.LBL_CONFIRM_PURCHASE not in verify_text.text:
            assert False, "Wrong PopUp displayed"
        values = re.findall(r"[\d.]*\d+", text)
        verify_text = pop_up.find_element_by_css_selector(".ui-widget-content")
        if movie not in verify_text.text:
            assert False, "Wrong movie ( {} ) to rent ".format(movie)
        if values[1] not in verify_text.text:
            assert False, "Wrong number of days to rent "
        if "$" + values[0] not in verify_text.text:
            assert False, "Wrong price"

    def assert_pop_up_not_present(self):
        self.assertElementNotPresentByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)
        self.assertElementNotPresentByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
        self.assertElementNotPresentByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS)

    def assert_player_present(self):
        self.assertElementNotPresentByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)
        self.assertElementNotPresentByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS)

    def assert_TVOD_offer_in_Watch_Now(self):
        self.assertElementPresentByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)

    def assert_TVOD_offer_displayed(self):
        if self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS):
            self.assertElementNotPresentByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS)
        else:
            self.assert_player_present()

    def verify_OnDemand_submenus(self):
        if Settings.mso.lower() == "cableco":
            self.log.info("Verify On Demand submenus")
            self.driver.clickElementByLinkText(OnDemandLabels.LBL_ON_DEMAND)
            self.log.info("\nI'm in navigate_on_demand_submenu\n")
            elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
            all_li = elem.find_elements_by_tag_name("li")
            for i in OnDemandLabels.LBL_ON_DEMAND_SUBMENUS:
                self.log.info("Verify {}".format(i))
                check = 0
                for li in all_li:
                    if i in li.get_attribute("textContent"):
                        check = 1
                if check == 0:
                    assert False, "The Submenu {} is not present".format(i)
            self.on_demandSubMenus()
        else:
            self.log.info("This method is not applied to this MSO ", Settings.mso)

    def assert_preview_btn_present(self):
        self.assertElementPresentByCSS(OnDemandLocators.LOC_Preview_BTN_CSS)

    def on_demandSubMenus(self):
        self.verify_TVNetworks()
        self.verify_TVSeries()
        self.verify_TiVo()
        self.verify_ArmstrongNeighborhood()
        self.verify_Kids()
        self.verify_Movies()
        self.verify_FreePrograms()
        self.verify_AllMovies()
        self.verify_HDonDemand()
        self.verify_Promotions()
        self.verify_NewReleases()
        self.verify_AdultOnDemand()
        self.verify_EventsOnDemand()
        self.verify_PremiumTV()
        self.verify_QE()

    def navigate_ondemand_submenu(self, text):
        self.log.info("\nI'm in navigate_on_demand_submenu\n")
        elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
        all_li = elem.find_elements_by_tag_name("li")
        for li in all_li:
            if text in li.get_attribute("textContent") and li.text in text:
                element = li.get_attribute("id")
                self.log.info("text: {}  id: {}".format(text, element))
                self.driver.clickElement(li)

    def verify_TVNetworks(self):
        self.log.info("I'm in verify_TVNetworks method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[0])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TV_NETWORKS_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_TV_NETWORK_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TV_NETWORK_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_TVSeries(self):
        self.log.info("I'm in verify_TVSeries method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[1])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TV_SERIES_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_TV_SERIES_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TV_SERIES_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_TiVo(self):
        self.log.info("I'm in verify_TiVo method.")
        elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
        all_li = elem.find_elements_by_tag_name("li")
        for li in all_li:
            if OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[2] in li.get_attribute("textContent")\
                    and li.text in OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[2]:
                element = li.text
                self.log.info("text: {}  id: {}".format(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[2], element))
                self.driver.clickElementByLinkText(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[2])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TiVo_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_TiVo_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_TiVo_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_ArmstrongNeighborhood(self):
        self.log.info("I'm in verify_Armstrong Neighborhood method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[3])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Armstrong_Neighborhood_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Armstrong_Neighborhood_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Armstrong_Neighborhood_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_Kids(self):
        self.log.info("I'm in verify_Kids method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[4])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Kids_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Kids_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Kids_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_Movies(self):
        self.log.info("I'm in verify_Movies method.")
        elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
        all_li = elem.find_elements_by_tag_name("li")
        for li in all_li:
            if OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5] in li.get_attribute("textContent")\
                    and li.text in OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5]:
                element = li.text
                self.log.info("text: {}  id: {}".format(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5], element))
                self.driver.clickElementByLinkText(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Movies_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Movies_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Movies_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_FreePrograms(self):
        self.log.info("I'm in verify_Free Programs method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[6])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Free_Programs_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Free_Programs_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Free_Programs_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_AllMovies(self):
        self.log.info("I'm in verify_All Movies method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[7])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_All_Movies_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_All_Movies_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_All_Movies_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_HDonDemand(self):
        self.log.info("I'm in verify_HD on Demand method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[8])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_HD_On_Demand_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_HD_On_Demand_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_HD_On_Demand_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_Promotions(self):
        self.log.info("I'm in verify_Promotions method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[9])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Promotions_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Promotions_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Promotions_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_NewReleases(self):
        self.log.info("I'm in verify_New Releases method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[10])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_New_Releases_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_New_Releases_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_New_Releases_STRIPS)

    def verify_AdultOnDemand(self):
        self.log.info("I'm in verify_Adult On Demand method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[11])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Adult_On_Demand_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Adult_On_Demand_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Adult_On_Demand_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_EventsOnDemand(self):
        self.log.info("I'm in verify_Events On Demand method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[12])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Events_On_Demand_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Events_On_Demand_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Events_On_Demand_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_PremiumTV(self):
        self.log.info("I'm in verify_Premium TV method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[13])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Premium_TV_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_Premium_TV_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_Premium_TV_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)

    def verify_QE(self):
        self.log.info("I'm in verify_QE method.")
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[14])
        self.driver.page_has_loaded(5)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_QE_ACTIVE_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(OnDemandLocators.LOC_QE_STRIPS)
        self.assertElementPresentByXpath(OnDemandLocators.LOC_QE_STRIPS)
        self.driver.waitUntilElementIsClickableByCSS(OnDemandLocators.LOC_STRIP, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_STRIP)
        self.assertElementPresentByCSS(OnDemandLocators.LOC_FEED)
