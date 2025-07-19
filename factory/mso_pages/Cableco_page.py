'''
Created on Jan 14, 2020

@author: mcretu
'''

from webportal.test_settings import WebPortalSettings
from webportal.client_api.base.locators import BaseLocators
from webportal.client_api.base.labels import BaseLabels
from webportal.client_api.what_to_watch.page import WhatToWatchPage
from webportal.client_api.search.page import SearchPage
from webportal.client_api.manage.page import ManagePage
from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.guide.page import GuidePage
from webportal.client_api.my_shows.locators import MyShowsLocators
from webportal.client_api.my_shows.page import MyShowsPage
from webportal.client_api.ondemand.page import OnDemandPage


class CablecoPage(WhatToWatchPage, SearchPage, ManagePage, GuidePage, MyShowsPage, OnDemandPage):

    def __init__(self, obj):
        self.driver = obj.driver
        self.log = obj.log

    def select_button_sign_in(self):
        self.log.info("Skip Click on Sign In button")

    def log_in(self):
        self.log.info("I'm in log_in() method. Enter credentials: user and password")
        self.driver.typeTextByXPath(WebPortalSettings.username, BaseLocators.LOC_USERNAME_LOGIN_FIELD_CABLECO_XPATH)
        self.driver.typeTextByXPath(WebPortalSettings.password, BaseLocators.LOC_PASSWORD_LOGIN_FIELD_CABLECO_XPATH)
        self.driver.clickElementByCSS(BaseLocators.LOC_LOG_IN_BUTTON_CABLECO_CSS)
        self.driver.handle_alert(True)  # handle Alert from Firefox Browser
        page_url = self.driver.page_has_loaded(10)
        self.handle_portalLogInIssues(page_url)
        self.driver.exit_banner()

    def select_UntilIDelete(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_Cableco_XPATH)

    def getShowsTitleList(self):
        self.log.info("### I'm in getShowsTitleList() method. ###")
        self.driver.refresh()
        self.log.info("== Select Folder 'Streaming Movies' ==")
        self.driver.clickElementByCSS(MyShowsLocators.LOC_STREAMING_CABLECO_MOVIES_CSS)
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MYSHOWS_CHECKBOX_CSS)
        myShowsList = self.driver.getElementsByCSS(MyShowsLocators.LOC_SHOW_ITEM_LIST_CSS)
        myShowsTitleList = list()
        for show in myShowsList:
            myShowsTitleList.append(
                self.driver.getElementFromParentByCSS(show, MyShowsLocators.LOC_SHOW_ITEM_TITLE_CSS).text)
        return myShowsTitleList
