from webportal.client_api.manage.locators import ManageLocators
from webportal.client_api.manage.labels import ManageLabels
from webportal.client_api.base.page import BasePage
from webportal.test_settings import WebPortalSettings as Settings


class ManagePage(BasePage):

    def go_to_Manage(self):
        self.driver.page_has_loaded(5)
        self.driver.waitUntilElementIsClickableByCSS(ManageLocators.LOC_MANAGE_CSS)
        self.driver.clickElementByLinkText(ManageLabels.LBL_MANAGE)

    def select_OnePass_Manager(self):
        self.driver.clickElementByLinkText(ManageLabels.LBL_ONEPASS_MANAGER)

    def select_OnePass(self):
        self.driver.waitUntilElementIsDisplayedByXpath(ManageLocators.LOC_ONEPASS_ITEM_RECORDINGS_XPATH)
        self.driver.waitUntilElementIsClickableByXpath(ManageLocators.LOC_ONEPASS_ITEM_RECORDINGS_XPATH)
        self.driver.clickElementByXPATH(ManageLocators.LOC_ONEPASS_ITEM_RECORDINGS_XPATH)

    def select_KeepUntil(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_OPTION_XPATH)

    def select_UntilIDelete(self):
        self.driver.clickElementByXPATH(ManageLocators.LOC_MODIFY_KEEPUNTIL_UNTILIDELETE_XPATH)

    def select_modify_OnePass_button(self):
        self.driver.clickElementByCSS(ManageLocators.LOC_MODIFY_ONEPASS_BUTTON_CSS)

    def delete_all_from_to_do_list(self):
        self.log.info("I'm in delete_all_from_to_do_list() method.")
        element = self.driver.waitUntilElementIsVisibleByCSS(ManageLocators.LOC_EMPTY_LIST_CSS)
        if element is None:
            self.log.info("To Do List was found with content. Proceed to manual deletion.")
            length = 1
            empty_list = None
            while length > 0 and empty_list is None:
                self.driver.clickElementByCSS(ManageLocators.LOC_TO_DO_LIST_EDIT_BUTTON_CSS)
                one_pass_list = self.driver.waitUntilElementsAreVisibleByCSS(ManageLocators.LOC_LIST_CONTENTS_CSS)
                if one_pass_list is not None:
                    length = len(one_pass_list)
                    self.log.info(f"One Pass List Elements Found : {length}")
                    for item in one_pass_list:
                        self.log.info(f"clicking on item {item.get_attribute('class')}...")
                        item.click()
                        self.driver.pause(0.2)
                    self.driver.clickElementByCSS(ManageLocators.LOC_TO_DO_LIST_DELETE_BUTTON_CSS)
                    self.driver.clickElementByCSS(ManageLocators.LOC_CANCEL_OK_BUTTON)
                    self.log.info(f"Deleted {length} elements from To Do List.")
                    empty_list = self.driver.waitUntilElementIsVisibleByCSS(ManageLocators.LOC_TO_DO_EMPTY_LIST,
                                                                            Settings.LOW_WAIT_TIME)
                else:
                    self.log.info("No One Pass Recordings in To-Do List. Nothing to do. Proceed to next test steps.")
                    length = 0
        else:
            self.log.info("To Do List was found empty. Nothing to do. Proceed to next test steps.")
