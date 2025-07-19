import pytest
from webportal.client_api.manage.assertions import ManageAssertions
from webportal.client_api.manage.page import ManagePage
from webportal.factory.factory import Factory


@pytest.fixture(scope="function")
def setup_manage(request):
    """
    Configure steps to be executed before the test cases run
    :param request:
    :return:
    """
    request.cls.manage_page = Factory.page_factory(request.cls)
    request.cls.manage_assertions = Factory.assertions_factory(request.cls)


@pytest.fixture(autouse=False, scope="function")
def setup_todolist_delete_all(request):
    request.cls.log.info(":::::::::::: I'm in setup - setup_todolist_delete_all - method :::::::::::: \n")
    request.cls.log.info("")
    request.cls.manage_page.select_button_sign_in()
    request.cls.manage_page.log_in()
    request.cls.log.info("")
    request.cls.manage_page.go_to_Manage()
    request.cls.log.info("")
    request.cls.manage_page.delete_all_from_to_do_list()
