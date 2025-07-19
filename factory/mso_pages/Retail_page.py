# coding=utf-8
'''
Created on Jan 14, 2020

@author: mcretu
'''
from webportal.test_settings import WebPortalSettings
from webportal.client_api.base.locators import BaseLocators
from webportal.client_api.base.labels import BaseLabels
from webportal.client_api.guide.page import GuidePage
from webportal.client_api.manage.page import ManagePage
from webportal.client_api.my_shows.page import MyShowsPage
from webportal.client_api.search.page import SearchPage
from webportal.client_api.what_to_watch.page import WhatToWatchPage
from webportal.client_api.ondemand.page import OnDemandPage


class RetailPage(GuidePage, ManagePage, MyShowsPage, SearchPage, WhatToWatchPage, OnDemandPage):
    def __init__(self, obj):
        self.driver = obj.driver
        self.log = obj.log
