import pytest
from webportal.client_api.guide.assertions import GuideAssertions
from webportal.client_api.guide.page import GuidePage
from webportal.client_api.guide.locators import GuideLocators
from webportal.factory.factory import Factory
from webportal.test_settings import WebPortalSettings as Settings


@pytest.fixture(scope="function")
def setup_guide(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.guide_page = Factory.page_factory(request.cls)
    request.cls.guide_assertions = Factory.assertions_factory(request.cls)


@pytest.fixture(autouse=False, scope="function")
def setup_recordable_channels(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_recordable_channels - method :::::::::::: \n")
    request.cls.recordable_channel = None
    if Settings.mso.lower() == "cableco":
        if Settings.hasRecordablechannels:
            request.cls.recordable_channel = request.cls.service_api.get_recordable_channels()
        else:
            request.cls.log.info("== Account is standalone or is unrecordable channel ==\n")
            pytest.skip("== Account is standalone or is unrecordable channel ==")
    else:
        request.cls.log.info(f"== Not applicable for mso {Settings.mso} ==\n")
