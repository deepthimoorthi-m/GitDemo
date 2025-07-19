# -*- coding: utf-8 -*-
from webportal.client_api.base.locators import BaseLocators


class ManageLocators(BaseLocators):

    LOC_COLAPSED_NAV_MENU_CSS = ".mobile-main-nav-menu-main"
    LOC_MANAGE_CSS = "#menu-link-id-manage"
    LOC_MANAGE_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and contains(@aria-labelledby," \
                                   " 'menu-link-id-manage')]"
    LOC_MANAGE_NAV_SUBMENU_XPATH = "//ul[contains(@style, 'display: block')]"
    LOC_ONEPASS_ITEM_XPATH = "//li[@class='manage-onepass-line']"
    LOC_ONEPASS_ITEM_RECORDINGS_XPATH = "//div[contains(@class, 'show-recording')]"
    LOC_MODIFY_ONEPASS_WINDOW_CSS = "[class='ui-dialog-title']"
    LOC_MODIFY_KEEPUNTIL_OPTION_XPATH = "//span[contains(@id, 'keepUntil-button')]//span[contains(@class, " \
                                        "'ui-selectmenu-text')]"
    LOC_MODIFY_KEEPUNTIL_UNTILIDELETE_XPATH = "//li[contains(@class, 'ui-') and contains(., 'Until I delete')]"
    LOC_MODIFY_ONEPASS_BUTTON_CSS = ".default-button.submit-button"
    LOC_MODIFY_ONEPASS_WHISPER_CSS = ".whisper-notification"
    LOC_CONFIRM_NEW_KEEPUNTIL_VALUE_XPATH = "//div[contains(@class, 'option')]/span[contains(@class, 'keepUntil')]"
    LOC_ONEPASS_XPATH = "//span[@class='js-title onepass-title']"

    LOC_TO_DO_LIST_XPATH = "//a[@id='menu-link-id-to-do-list']"
    LOC_TO_DO_LIST_MESSAGE = "//p[contains(text(),'Sign in to schedule recordings.')]"
    LOC_ONEPASS_MANAGER = "//a[@id='menu-link-id-onepass-manager']"
    LOC_ONEPASS_MANAGER_BROWSER_MESSAGE = "//p[contains(text(),'Sign in to manage your OnePass selections. " \
                                          "Reprioritize, delete, or even copy a OnePass to another TiVo box!')]"
    LOC_ONEPASS_QUICK_SELECT = "//a[@id='menu-link-id-onepass-quick-select']"
    LOC_ONEPASS_QUICK_SELECT_MESSAGE = "//p[contains(text(),'Sign in to create and manage your OnePass selections" \
                                       " for your favorite shows.')]"
    LOC_RECORDING_ACTIVITY = "//a[@id='menu-link-id-recording-activity']"
    LOC_RECORDING_ACTIVITY_BROWSER_MESSAGE = "//p[contains(text(),'Sign in to access your recording activity.')]"
    LOC_MANAGE_PAGE_CSS = "#menu-link-id-manage"
    LOC_TO_DO_LIST = "#ui-id-30"
    LOC_TO_DO_LIST_ID = "#menu-link-id-to-do-list"
    LOC_TO_DO_LIST_CSS = "[class ='js-todo-list todo-list-wrapper ui-selectable']"
    LOC_TO_DO_LIST_MESSAGE_CSS = ".info-message"
    LOC_TO_DO_LIST_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and " \
                                       "contains(@aria-labelledby,'menu-link-id-to-do-list')]"
    LOC_ACTIVE = """//li[a[@id='menu-link-id-to-do-list']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""

    LOC_ONE_PASS_QUICK_SELECT_CSS = "#menu-link-id-onepass-quick-select"
    LOC_QUICK_MESSAGE_CSS = ".bulk-onepass-header"

    LOC_RECORDING_ACTIVITY_CSS = "#menu-link-id-recording-activity"
    LOC_RECORDING_ACTIVITY_MESSAGE = ".description-message"

    LOC_ONEPASS_MANAGER_CSS = "#menu-link-id-onepass-manager"
    LOC_ONEPASS_MANAGER_MESSAGE = ".manage-onepass-nav-bar"

    LOC_WHAT_TO_WATCH = ".nav-menu-item.link-primary"
    LOC_JUST_FOR_ME = "#menu-link-id-just-for-me"

    LOC_BOX_UI = ".help-menu-list-item.isDVR"
    LOC_TRANSFER_RECORDINGS = "#menu-link-id-transfer-recordings"
    LOC_TRANSFER_REC_MESSAGE = ".default-message.hide-for-single-dvr"

    LOC_TO_DO_LIST_GRID = "[class='js-todo-list todo-list-wrapper ui-selectable']"
    LOC_ONE_PASS_GRID = ".multi-list-container"
    LOC_QUICK_PASS_GRID = ".items"
    LOC_RECORDING_ACTIVITY_GRID = ".js-history-list-view"
    LOC_TRANSFER_GRID = ".js-transfer-list-view"

    LOC_TO_DO_LIST_ASSET_NAME_CSS = ".todo-episode-title"
    LOC_CANCEL_RECORDING_CSS = ".ui-dialog-title"
    LOC_CANCEL_OK_BUTTON = "[class='default-button confirmation-button']"
    LOC_LIST_CONTENTS_CSS = ".onepass-line"
    LOC_TO_DO_EMPTY_LIST = "[class='default-message todo-empty-list']"

    # Cableco
    LOC_MODIFY_KEEPUNTIL_Cableco_XPATH = "//li[contains(@class, 'ui-') and contains(., 'As long as possible')]"
