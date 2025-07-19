import pytest
import os
import glob

from core_api.web import driverfactory
from webportal.test_settings import WebPortalSettings as Settings
from tools.logger.logger import Logger
from mind_api.middle_mind.api_helper import ApiHelper
from mind_api.middle_mind.service_api import ServiceAPI
from webportal.client_api.base.locators import BaseLocators
from mind_api.middle_mind.device_provisioning_api_helper import DeviceProvisioningApiHelper


logger = Logger(__name__)


def pytest_addoption(parser):
    parser.addoption("--log_path", default=Settings.log_path, action="store", dest="log_path", help="Path to store Log File")
    parser.addoption("--TENANT", default=Settings.TENANT, action="store", dest="TENANT", help="TENANT")
    parser.addoption("--username", default=Settings.username, action="store", dest="username", help="username")
    parser.addoption("--password", default=Settings.password, action="store", dest="password", help="password")
    parser.addoption("--browser", default=Settings.browser, action="store", dest="browser", help="Browser type")
    parser.addoption("--driver_type", default=Settings.driver_type, action="store", dest="driver_type", help="driver type")
    parser.addoption("--tsn", default=Settings.tsn, action="store", dest="tsn", help="TSN of the device")
    parser.addoption("--mso", default=Settings.tsn, action="store", dest="mso", help="MSO of the device")
    parser.addoption("--headless", default=Settings.headless, action="store", dest="headless",
                     help="Enable headless mode for supported browsers.")
    parser.addoption("--test_environment", default=Settings.test_environment, action="store", dest="test_environment",
                     help="Test environment of the STB: staging, usqe1, prod")
    parser.addoption("--hasRecordablechannels", default=Settings.hasRecordablechannels, action="store",
                     dest="hasRecordablechannels", help="hasRecodablechannels flag")
    parser.addoption("--ca_device_id", default=Settings.ca_device_id, action="store",
                     dest="ca_device_id", help="ca_device_id")
    parser.addoption("--pcid", default=Settings.pcid, action="store",
                     dest="pcid", help="partnerCustomerId")
    return parser


def pytest_configure(config):
    if config.getoption("mso"):
        Settings.mso = config.getoption("mso")
    if config.getoption("TENANT"):
        Settings.TENANT = config.getoption("TENANT")
    if config.getoption("TENANT"):
        Settings.username = config.getoption("username")
    if config.getoption("username"):
        Settings.password = config.getoption("password")
    if config.getoption("log_path"):
        Settings.log_path = config.getoption("log_path")
    if config.getoption("browser"):
        Settings.browser = config.getoption("browser")
    if config.getoption("driver_type"):
        Settings.driver_type = config.getoption("driver_type")
    if config.getoption("tsn"):
        Settings.tsn = config.getoption("tsn")
    if config.getoption("headless"):
        Settings.headless = config.getoption("headless")
    if config.getoption("test_environment"):
        Settings.test_environment = config.getoption("test_environment")
    if config.getoption("hasRecordablechannels"):
        Settings.hasRecordablechannels = config.getoption("hasRecordablechannels")
    if config.getoption("pcid"):
        Settings.pcid = config.getoption("pcid")
    if config.getoption("ca_device_id"):
        Settings.ca_device_id = config.getoption("ca_device_id")


@pytest.fixture(autouse=True, scope="function")
def initialize_driver(request):
    logger.info("")
    logger.info("::::::::::: Initialize Driver :::::::::::::::")
    logger.info("")

    driver_config = driverfactory.DriverConfig(
        driver_type=Settings.driver_type,
        log_path=Settings.log_path,
        browser=Settings.browser,
        driver_config=Settings.driver_type,
        TENANT=Settings.TENANT,
        tsn=Settings.tsn,
        headless=Settings.headless)

    request.cls.driver = driverfactory.DriverFactory.create_driver(driver_config)
    request.cls.driver.start()
    request.config.Settings = Settings
    request.cls.api = ApiHelper(mso=Settings.mso, device_type="webportalstb")
    request.cls.service_api = ServiceAPI(mso=Settings.mso, device_type="webportalstb")
    request.cls.log = logger


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        feature_request = item.funcargs['request']
        if report.passed:
            # remove png for passed TC
            clean_up_png(Settings.log_path, feature_request.node.name)
        elif report.outcome in 'failed':
            logger.info("Take Screenshot because test failed...")
            file_name = feature_request.cls.driver.take_screenshot(feature_request.node.name, Settings.log_path)
            extra.append(pytest_html.extras.image(file_name, ''))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


def clean_up_png(path, testcase_name, extension="png", all_png=False):
    """
    method to remove artifacts related to TC.

    Args:
        path: str, path where cleaning will performed
        testcase_name: str, name of TC (substring of filename to be removed)
        extension: str, extension of files to be removed
        all_png: bool, if True than all files will be removed else except one last

    """
    if all_png:
        logger.info(f"Remove all PNGs for passed TC: {format(testcase_name)}")
    else:
        logger.info(f"Remove old PNGs for passed TC: {format(testcase_name)}. Keep the last PNG (most recent one).")

    list_of_png = glob.glob1(path, "*{}*.{}".format(testcase_name, extension))
    if list_of_png:
        list_of_png.sort()
        png_to_be_removed = list_of_png if all_png else list_of_png[:-1]
        logger.debug(f"Found a list of PNGs:\n {list_of_png}")
        logger.debug(f"{len(png_to_be_removed)} PNG to be removed: {png_to_be_removed}")
        try:
            for png_file in png_to_be_removed:
                os.remove(os.path.join(path, png_file))
        except Exception as err:
            logger.error("Error raised while cleaning up: {}".format(err))
    else:
        logger.info("Nothing to remove for TC: {}".format(testcase_name))


@pytest.fixture(autouse=True, scope="session")
def add_loggers(request):
    """
    The fixture to configure loggers
    It uses built-in pytest arguments to configure loggigng level and files

        Parameters:
            log_level or --log-level general log level for capturing
            log_file_level or --log-file-level  level of log to be stored to a file. Usually lower than general log
            log_file or --log-file  path where logs will be saved
    """
    log_level = request.config.getini("log_level") or request.config.getoption("--log-level") or "INFO"
    log_file_level = request.config.getini("log_file_level") or request.config.getoption("--log-file-level") or "DEBUG"
    log_file = request.config.getini("log_file") or request.config.getoption("--log-file")
    if not log_file:
        log_file = os.path.join(os.path.abspath(Settings.log_path), "pytest.log")
    else:
        log_file = os.path.abspath(log_file)
    logger.info("General loglevel: '{}', File: '{}'".format(log_level, log_file_level))
    logger.info("Test's logs will be stored: '{}'".format(log_file))
    logger.setup_cli_handler(level=log_level)


@pytest.fixture(autouse=True)
def test_case_logger(request):
    logger.info("")
    logger.info("::::::::::: Test case name start: {} :::::::::::::::".format(request.node.name))
    logger.info("")

    yield

    logger.info("")
    logger.info("::::::::::: Test case name end: {} :::::::::::::::".format(request.node.name))
    logger.info("")


@pytest.fixture(autouse=True, scope="function")
def postcondition(request):

    def logout():
        try:
            logger.info("::::::::::: Logout after test execution :::::::::::")
            logger.info("Verify if need to perform 'Sign Out'.")
            element = request.cls.driver.waitUntilElementIsDisplayedByCSS(BaseLocators.LOC_SIGN_OUT_BUTTON_CSS)
            if element is not None:
                logger.info("Currently Signed In. Performing 'Sign Out'...")
                request.cls.driver.log_out()
            else:
                logger.info("Currently Signed Out. Nothing to do. Continue with the next test.")

            logger.info("")
            logger.info("::::::::::: Close Driver (Close Browser Instances) :::::::::::::::")
            logger.info("")
            request.cls.driver.teardown()

        except Exception as error:
            logger.error("Finalization of is failed with error '{}'".format(error))

    request.addfinalizer(logout)
