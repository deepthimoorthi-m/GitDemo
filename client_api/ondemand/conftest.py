import pytest
from webportal.factory.factory import Factory


@pytest.fixture(scope="function")
def setup_ondemand(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.ondemand_page = Factory.page_factory(request.cls)
    request.cls.ondemand_assertions = Factory.assertions_factory(request.cls)
