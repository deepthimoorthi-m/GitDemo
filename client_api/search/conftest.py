import pytest
from webportal.client_api.search.assertions import SearchAssertions
from webportal.client_api.search.page import SearchPage
from webportal.factory.factory import Factory


@pytest.fixture(scope="function")
def setup_search(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.search_page = Factory.page_factory(request.cls)
    request.cls.search_assertions = Factory.assertions_factory(request.cls)
