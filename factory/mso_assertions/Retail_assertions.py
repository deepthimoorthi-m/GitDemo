# coding=utf-8
'''
Created on Jan 14, 2020

@author: mcretu
'''
from webportal.client_api.guide.assertions import GuideAssertions
from webportal.client_api.manage.assertions import ManageAssertions
from webportal.client_api.my_shows.assertions import MyShowsAssertions
from webportal.client_api.search.assertions import SearchAssertions
from webportal.client_api.what_to_watch.assertions import WhatToWatchAssertions
from webportal.client_api.ondemand.assertions import OnDemandAssertions


class RetailAssertions(GuideAssertions, ManageAssertions, MyShowsAssertions, SearchAssertions, WhatToWatchAssertions,
                       OnDemandAssertions):

    def __init__(self, obj):
        self.driver = obj.driver
        self.log = obj.log
