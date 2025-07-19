from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.manage.labels import ManageLabels
from webportal.client_api.base.assertions import BaseAssertions
from webportal.test_settings import WebPortalSettings as Settings
from webportal.client_api.base.locators import BaseLocators


class ManageAssertions(BaseAssertions):

    def assert_Manage(self):
        self.assertTextPresent(ManageLabels.LBL_MANAGE)

    def assert_Modify_OnePass(self):
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_MODIFY_ONEPASS_XPATH, Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByXPATH(ManageLocators.LOC_MODIFY_ONEPASS_XPATH)
        self.log.info('MODIFY button is present')

    def assert_Modify_displayed(self):
        self.driver.waitUntilElementIsVisibleByCSS(ManageLocators.LOC_MODIFY_ONEPASS_WINDOW_CSS)
        self.assertElementPresentByCSS(ManageLocators.LOC_MODIFY_ONEPASS_WINDOW_CSS)
        self.log.info('MODIFY OnePass window is present')

    def assert_KeepUntil_value(self):
        self.assertElementPresentByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.assertLabelPresentByXpath('Space needed', ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.log.info('The default include value: "Space needed" is correct')

    def assert_KeepUntil_value_selected(self):
        self.assertElementPresentByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.assertLabelPresentByXpath('Until I delete', ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)
        self.log.info('The changed include value: "Until I delete" is correct')

    def assert_Modify_Whisper_OnePass(self):
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_MODIFY_ONEPASS_WHISPER_CSS,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertElementPresentByCSS(ManageLocators.LOC_MODIFY_ONEPASS_WHISPER_CSS)
        self.assertLabelPresentByCSS(ManageLabels.LBL_MODIFY_ONEPASS_WHISPER,
                                     ManageLocators.LOC_MODIFY_ONEPASS_WHISPER_CSS)
        self.log.info('OnePass Modify whisper was displayed and the text is correct')
        self.driver.waitUntilElementIsNotVisibleByCSS(ManageLocators.LOC_MODIFY_ONEPASS_WHISPER_CSS,
                                                      Settings.HIGH_WAIT_TIME)

    def assert_value_selected_OnePass(self):
        self.driver.waitUntilElementIsVisibleByXpath(ManageLocators.LOC_CONFIRM_NEW_KEEPUNTIL_VALUE_XPATH,
                                                     Settings.HIGH_WAIT_TIME)
        self.assertLabelPresentByXpath("Until I delete", ManageLocators.LOC_CONFIRM_NEW_KEEPUNTIL_VALUE_XPATH)
        self.log.info("New Keep Until option: 'Until I delete' is changed")

    def assert_Asset_with_OnePass(self, showName):
        # using lower to compare show name, as sometimes the show name in WTW is using capital and in Manage, it isn't
        self.log.info(f"Verify if '{showName}' is displayed in Manage page")
        self.assertLabelPresentByCSS(showName, '[class="channel-title"]')
        self.log.info(f'{showName} is displayed in Manage page')

    def manage_to_do_list(self):
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_TO_DO_LIST_XPATH, Settings.HIGH_WAIT_TIME)
        self.driver.clickElementByXPATH(ManageLocators.LOC_TO_DO_LIST_XPATH)
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_TO_DO_LIST_MESSAGE)
        self .assertElementPresentByXPATH(ManageLocators.LOC_TO_DO_LIST_MESSAGE)

    def manage_onepass_manager(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_ONEPASS_MANAGER)
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_ONEPASS_MANAGER_BROWSER_MESSAGE)
        self.assertElementPresentByXPATH(ManageLocators.LOC_ONEPASS_MANAGER_BROWSER_MESSAGE)

    def manage_onepass_quick_select(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_ONEPASS_QUICK_SELECT)
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_ONEPASS_QUICK_SELECT_MESSAGE)
        self.assertElementPresentByXPATH(ManageLocators.LOC_ONEPASS_QUICK_SELECT_MESSAGE)

    def manage_recording_activity(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_RECORDING_ACTIVITY)
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_RECORDING_ACTIVITY_BROWSER_MESSAGE)
        self.assertElementPresentByXPATH(ManageLocators.LOC_RECORDING_ACTIVITY_BROWSER_MESSAGE)

    def managePageSubMenus(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_MANAGE_PAGE_CSS)
        self.verify_manageToDoListPage()
        self.verify_manageOnePassManagerPage()
        self.verify_manageOnePassQuickSelectPage()
        self.verify_manageRecordingActivityPage()
        self.verify_manageTransferPage()

    def verify_manageToDoListPage(self):
        self.log.info("== Expectance: Verify that the To Do List submenu is active and is successfully displayed. ==")
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_ACTIVE)
        self.assertElementPresentByXPATH(ManageLocators.LOC_ACTIVE)
        self.driver.clickElementByCSS(ManageLocators.LOC_TO_DO_LIST_ID)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_TO_DO_LIST_MESSAGE_CSS)
        self.assertElementPresentByCSS(ManageLocators.LOC_TO_DO_LIST_MESSAGE_CSS)
        element = self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_TO_DO_LIST_GRID)
        if element is None:
            empty_list = self.driver.waitUntilElementIsVisibleByCSS(ManageLocators.LOC_TO_DO_EMPTY_LIST,
                                                                    Settings.LOW_WAIT_TIME)
            self.assertElementPresentByCSS(ManageLocators.LOC_TO_DO_EMPTY_LIST)
            self.log.info(f"'Manage' - 'To Do List' was found empty:\n'{empty_list.text}'")
        else:
            self.assertElementPresentByCSS(ManageLocators.LOC_TO_DO_LIST_GRID)
            self.log.info("'Manage' - 'To Do List' was found with content.")

    def verify_manageOnePassManagerPage(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_ONEPASS_MANAGER_CSS)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_ONEPASS_MANAGER_MESSAGE)
        self.assertElementPresentByCSS(ManageLocators.LOC_ONEPASS_MANAGER_MESSAGE)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_ONE_PASS_GRID)
        self.assertElementPresentByCSS(ManageLocators.LOC_ONE_PASS_GRID)

    def verify_manageOnePassQuickSelectPage(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_ONE_PASS_QUICK_SELECT_CSS)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_QUICK_MESSAGE_CSS)
        self.assertElementPresentByCSS(ManageLocators.LOC_QUICK_MESSAGE_CSS)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_QUICK_PASS_GRID)
        self.assertElementPresentByCSS(ManageLocators.LOC_QUICK_PASS_GRID)

    def verify_manageRecordingActivityPage(self):
        self.driver.waitUntilElementIsClickableByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_CSS)
        self.driver.clickElementByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_CSS)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_MESSAGE)
        self.assertElementPresentByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_MESSAGE)
        self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_GRID)
        self.assertElementPresentByCSS(ManageLocators.LOC_RECORDING_ACTIVITY_GRID)

    def verify_manageTransferPage(self):
        elements = self.driver.getElementsByCSS(ManageLocators.LOC_BOX_UI)
        if len(elements) >= 2:
            self.driver.clickElementByCSS(ManageLocators.LOC_TRANSFER_RECORDINGS)
            self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_TRANSFER_REC_MESSAGE)
            self.assertElementPresentByCSS(ManageLocators.LOC_TRANSFER_REC_MESSAGE)
            self.driver.waitUntilElementIsDisplayedByCSS(ManageLocators.LOC_TRANSFER_GRID)
            self.assertElementPresentByCSS(ManageLocators.LOC_TRANSFER_GRID)

    def verify_logoClick(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_LOGO_CSS)
        self.driver.exit_banner()
        self.assertElementPresentByCSS(ManageLocators.LOC_JUST_FOR_ME)

    def assert_Manage_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_MANAGE_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(ManageLocators.LOC_MANAGE_HIGHLIGHTED_XPATH)
        self.log.info("Manage menu item and is highlighted")

    def assert_ToDoList_highlighted(self):
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_TO_DO_LIST_HIGHLIGHTED_XPATH)
        self.assertElementPresentByXpath(ManageLocators.LOC_TO_DO_LIST_HIGHLIGHTED_XPATH)
        self.log.info("To Do List menu item and is highlighted")

    def verify_to_do_list_recorded_element_present(self, recorded_asset, big_episode_name, episode_number, episode_name):
        if Settings.mso.lower() == "retail":
            show_name = recorded_asset + " " + episode_number + episode_name
            show_name_1 = big_episode_name
            try:
                self.assertLabelPresentByCSS(show_name, ManageLocators.LOC_TO_DO_LIST_ASSET_NAME_CSS)
                self.log.info("Element is Displayed in To-Do-List")
            except Exception:
                xpath = "//*[contains(text(),'" + show_name_1 + "')]"
                self.log.info("xpath : " + xpath)
                self.assertElementPresentByXpath(xpath)
                self.log.info("Element is Displayed in the To-Do-List")
        else:
            show_name = recorded_asset
            xpath = "//*[contains(text(),'" + show_name + "')]"
            self.log.info("xpath : " + xpath)
            self.assertElementPresentByXpath(xpath)
            self.log.info("Element is Displayed in the To-Do-List")
