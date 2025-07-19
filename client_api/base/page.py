from core_api.web.selenium.basedriver import BaseDriver
from webportal.client_api.base.locators import BaseLocators
from webportal.client_api.base.labels import BaseLabels
from webportal.test_settings import WebPortalSettings


class BasePage:

    def scroll_till_page_end(self):
        self.driver.scroll_page_by_pixel("document.body.scrollHeight")
        self.driver.page_has_loaded(5)

    def select_button_sign_in(self):
        self.driver.clickElementByCSS(BaseLocators.LOC_SIGN_IN_BUTTON_CSS)
        self.verify_PageLoginLoaded()

    def verify_PageLoginLoaded(self):
        self.log.info("I'm in verify_PageLoginLoaded() method")
        self.driver.page_has_loaded(5)
        for k in range(5):  # try redirect for five times - due to slowness of webportal
            self.log.info(f"== Check for login page loaded {k}/5 ==")
            element = self.driver.waitUntilElementIsClickableByXpath(BaseLocators.LOC_USERNAME_LOGIN_FIELD_XPATH,
                                                                     WebPortalSettings.HIGH_WAIT_TIME)
            if element is None:
                self.log.info("== LoginPage is not loaded. Try again: Refresh and wait for page to load... ==")
                self.driver.refresh()
                self.driver.page_has_loaded(5)
                self.driver.clickElementByXPATH(BaseLocators.LOC_WTW_SIGN_IN_GTS_XPATH)
            else:
                break
        if element is None:
            self.log.error("== LoginPage could not be loaded. ==")
            assert False, "== LoginPage could not be loaded. =="
        self.log.info("== LoginPage is loaded. ==")

    def log_in(self):
        self.log.info("I'm in log_in() method. Enter credentials: user and password")
        self.driver.typeTextByXPath(WebPortalSettings.username, BaseLocators.LOC_USERNAME_LOGIN_FIELD_XPATH)
        self.driver.typeTextByXPath(WebPortalSettings.password, BaseLocators.LOC_PASSWORD_LOGIN_FIELD_XPATH)
        self.driver.clickButtonByText(BaseLabels.LBL_LOG_IN, BaseLocators.LOC_LOG_IN_BUTTON_CSS)
        self.driver.handle_alert(True)  # handle Alert from Firefox Browser
        self.select_linked_box()

    def log_out(self):
        self.driver.waitUntilElementIsDisplayedByCSS(BaseLocators.LOC_MENU_ICON_MAIN_CSS)
        self.driver.clickElementByCSS(BaseLocators.LOC_MENU_ICON_MAIN_CSS)
        self.driver.waitUntilElementIsDisplayedByCSS(BaseLocators.LOC_SIGN_OUT_BUTTON_CSS)
        self.driver.clickButtonByText(BaseLabels.LBL_SIGN_OUT, BaseLocators.LOC_SIGN_OUT_BUTTON_CSS)
        self.driver.exit_banner()

    def select_linked_box(self):
        retry = 0
        max_retries = 3

        while retry < max_retries:
            box_item = self.extract_linked_box()
            if 'notselectable' in str(box_item.get_attribute("class")):
                retry = retry + 1
                self.log.warning(f"== Box found but is not selectable. Refresh page and try again {retry}/{max_retries} ==")
                self.driver.refresh()
                self.driver.page_has_loaded()
            else:
                break

        if 'notselectable' in str(box_item.get_attribute("class")):  # if box still not selectable after max_retries - fail
            self.log.error("Box found but is not selectable.")
            assert False, "Box found but is not selectable."
        self.click_linked_box(box_item)

    def handle_portalLogInIssues(self, page_url):
        """
        Handle web portal issues that can block automation testing.
        ie:
        security warning:
            https://jira.tivo.com/browse/CA-7245
            https://jira.tivo.com/browse/CA-7290
        login failed:
            https://jira.tivo.com/browse/PORTAL-10248
        """
        self.log.info("I'm in handle_portalLogInIssues() method.")

        # the handle take action when browser reach to an unexpected page
        portal_to_check = WebPortalSettings.TENANT + "/watch/feedList/JustForMeTVE"
        SecurityWarningURL = WebPortalSettings.TENANT + "sso"
        SignInFailedURL = WebPortalSettings.TENANT + "sso_complete?failed=true"
        DeviceLimitURL = WebPortalSettings.TENANT + "errorpages/device-limit"
        if page_url.lower() != portal_to_check.lower():
            self.log.info("Handle ON: Landed on unknown web page. Try to figure what to to.")
            if page_url.lower() != SignInFailedURL.lower() and \
                    page_url.lower() != SecurityWarningURL.lower() and page_url.lower() != DeviceLimitURL.lower():
                self.log.warning(f"Handle cannot be used! Don't know what to do on this page: '{page_url}'")

            # handle an issue that appears in chrome browsers only
            if WebPortalSettings.browser.lower() == "google-chrome":
                if page_url.lower() == SecurityWarningURL.lower():
                    self.log.warning(f"\n Expected Page: {WebPortalSettings.TENANT} \n"
                                     f" Actual Page, Security Warning URL: {page_url}")
                    if self.driver.isElementDisplayedByCSS(BaseLocators.LOC_INSECURE_FORM_CSS):
                        self.driver.clickElementById(BaseLocators.LOC_INSECURE_FORM_PROCEED_ID)
                    page_url = self.driver.page_has_loaded()

            # handle an issue that appears in all browsers
            if page_url.lower() == SignInFailedURL.lower():
                self.log.warning(f"\n Expected Page: {WebPortalSettings.TENANT} \n"
                                 f" Actual Page, SignIn Failed URL: {page_url}")
                element = self.driver.waitUntilElementIsVisibleByCSS(BaseLocators.LOC_LOGIN_FAILED_CSS)
                if element.text != BaseLabels.LBL_LOGIN_FAILED_MSG:
                    self.log.warning(f"Expected text on SignIn Failed page: '{BaseLabels.LBL_LOGIN_FAILED_MSG}'\n"
                                     f"Actual text is: '{element.text}'")
                self.driver.modify_cookies(WebPortalSettings.ca_device_id)
                self.driver.clickElementByCSS(BaseLocators.LOC_LOGIN_FAILED_SIGNINBTN_CSS)
                self.driver.typeTextByXPath(WebPortalSettings.username, BaseLocators.LOC_USERNAME_LOGIN_FIELD_CABLECO_XPATH)
                self.driver.typeTextByXPath(WebPortalSettings.password, BaseLocators.LOC_PASSWORD_LOGIN_FIELD_CABLECO_XPATH)
                self.driver.clickElementByCSS(BaseLocators.LOC_LOG_IN_BUTTON_CABLECO_CSS)
                page_url = self.driver.page_has_loaded()

            # handle Device limit error message
            if page_url.lower() == DeviceLimitURL.lower():
                self.log.warning(f"\n Expected Page: {WebPortalSettings.TENANT} \n"
                                 f" Actual Page, SignIn Failed URL: {page_url}")
                self.driver.modify_cookies(WebPortalSettings.ca_device_id)
                self.driver.start()
                self.driver.typeTextByXPath(WebPortalSettings.username, BaseLocators.LOC_USERNAME_LOGIN_FIELD_CABLECO_XPATH)
                self.driver.typeTextByXPath(WebPortalSettings.password, BaseLocators.LOC_PASSWORD_LOGIN_FIELD_CABLECO_XPATH)
                self.driver.clickElementByCSS(BaseLocators.LOC_LOG_IN_BUTTON_CABLECO_CSS)
                page_url = self.driver.page_has_loaded()

            # check that using handles above we reach on the intended page
            if page_url.lower() != portal_to_check.lower():
                assert False, f"End-up on an unknown page!\n" \
                              f"\tExpected: {portal_to_check}\n" \
                              f"\tActual: {page_url}"
        else:
            self.log.info("Handle OFF: No need for handle.")

    def extract_linked_box(self):
        """
        This function selects automatically after login, the linked box to the actual account.
        Box is selected based on the account and tsn given in line command of the test run
        :return: nothing
        """
        self.log.info("I'm in select_linked_box() method.")

        if self.driver.config.tsn == '':
            self.log.warning(f"No TSN was provided. Continue with "
                             f"the default box linked to current account {self.driver.settings.username}")

        page_url = self.driver.page_has_loaded()
        self.handle_portalLogInIssues(page_url)

        self.driver.clickElementByCSS(BaseLocators.LOC_HELP_MENU_MAIN_CSS)
        self.driver.waitUntilElementIsVisibleByXpath(BaseLocators.LOC_HELP_MENU_LIST_XPATH)
        self.driver.page_has_loaded()

        # 1. Get boxes linked to account
        box_items = self.get_boxes_linked_to_current_account(WebPortalSettings.MID_WAIT_TIME)

        # 2. Get the box based on its TSN
        box_item = self.get_box_from_list_of_boxes(box_items)

        return box_item

    def get_boxes_linked_to_current_account(self, timeout=WebPortalSettings.LOW_WAIT_TIME):
        self.log.info("Find boxes linked to current account.")
        boxesInAccount = 0
        while boxesInAccount < 1 and timeout > 0:
            self.driver.pause(1)  # wait one second
            html_list = self.driver.getElementByXPath(BaseLocators.LOC_HELP_MENU_LIST_XPATH)
            items = html_list.find_elements_by_tag_name("li")
            boxesInAccount = len(items) - 1
            timeout = timeout - 1
            if boxesInAccount == 0:
                self.log.info(f"No box found. Try again in one second. {timeout} tries left")
            else:
                self.log.info(f"Number of boxes found linked in account: {boxesInAccount}")
                break
        assert boxesInAccount > 0 or timeout > 0, f"Cant find boxes linked to current account {self.driver.settings.username}"
        return items

    def get_box_from_list_of_boxes(self, items):
        self.log.info(f"Looking for Box having TSN: {self.driver.config.tsn} in list of boxes available in the account.")
        box_found = False
        for item in items:
            # if 8D9000190315BF8 in tsn:8D9000190315BF8
            if str(self.driver.settings.tsn) in str(item.get_attribute("data-bodyid")):
                box_found = True
                break
        assert box_found, f"Box {self.driver.settings.tsn} NOT found to be linked " \
                          f"to selected account {self.driver.settings.username} !"
        self.log.info(f"Box found: {self.driver.settings.tsn} - {item.text}")
        return item

    def click_linked_box(self, box):
        box_name = getattr(box, 'text', '== Unknown ==')
        self.log.info(f"Select STB for test: {self.driver.settings.tsn} - {box_name}")

        try:
            box.click()
        except Exception as err:
            self.log.error(f"Could not click on box name '{box_name}'. Error: {err}")
            assert False, f"Could not click on box name '{box_name}'. Error: {err}"

        self.log.info(f"Successfully selected '{box_name}' box.")
        self.driver.page_has_loaded()

    def select_Modify(self):
        self.driver.clickElementByXPATH(BaseLocators.LOC_MODIFY_ONEPASS_XPATH)

    def select_tile_from_strip(self, strip_name=BaseLabels.LBL_WTW_STRIP_KIDS):
        self.log.info("I'm in select_tile_from_strip() method")
        strip = self.get_strip_from_wtw(strip_name)
        tile_list = self.get_tile_list_from_strip(strip)
        tile_from_strip = tile_list[0]  # take first tile for now. Later can be extended to take a custom one
        self.driver.scroll_to_element_from_page(tile_from_strip)
        self.log.info("Try to click a tile from strip")
        tile_from_strip_css = f"[class='{tile_from_strip.get_attribute('class')}']"
        self.driver.clickElementByCSS(tile_from_strip_css)

    def get_tile_list_from_strip(self, strip):
        self.log.info("I'm in get_tile_list_from_strip()")
        tile_list = strip.find_elements_by_tag_name("li")
        if tile_list is None:
            self.log.error("No tiles was found for selected strip.")
            assert False, "No tiles was found for selected strip."
        if type(tile_list) is list:  # if is list
            if not tile_list:  # if list empty
                self.log.error("Tile list was returned but no tiles was found in it.")
                assert False, "Tile list was returned but no tiles was found in it."
            else:
                return tile_list  # return list with elements
        self.log.warning("Tile list is not a list. Is a scalar.")
        return tile_list

    def get_strip_from_wtw(self, strip_name):
        self.log.info("I'm in get_strip_from_wtw() method")
        self.driver.page_has_loaded()
        if WebPortalSettings.mso.lower() == "cableco":
            elements = self.driver.waitUntilElementsAreVisibleByXpath(BaseLocators.LOC_WTW_STRIPS_XPATH)
        else:
            elements = self.driver.waitUntilElementsAreVisibleByCSS(BaseLocators.LOC_WTW_STRIPS)
        if elements is None:
            self.log.error("No strips was found in page.")
            assert False, "No strips was found in page."
        found = False
        for item in elements:
            if strip_name.lower() in item.text.lower():
                found = True
                return item
        if not found:
            self.log.error(f"Strip '{strip_name}' was not found among wtw page strips.")
        assert found, f"Strip '{strip_name}' was not found among wtw page strips."
