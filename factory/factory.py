from webportal.test_settings import WebPortalSettings
from webportal.factory.mso_pages.Retail_page import RetailPage
from webportal.factory.mso_pages.Cableco_page import CablecoPage
from webportal.factory.mso_assertions.Retail_assertions import RetailAssertions
from webportal.factory.mso_assertions.Cableco_assertions import CablecoAssertions


class Factory(object):

    def page_factory(default_obj):
        if WebPortalSettings.mso.lower() == "cableco":
            return CablecoPage(default_obj)
        else:
            return RetailPage(default_obj)

    def assertions_factory(default_obj):
        if WebPortalSettings.mso.lower() == "cableco":
            return CablecoAssertions(default_obj)
        else:
            return RetailAssertions(default_obj)
