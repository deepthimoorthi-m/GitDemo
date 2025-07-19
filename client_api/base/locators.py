# -*- coding: utf-8 -*-


class BaseLocators:
    LOC_SIGN_IN_BUTTON_CSS = "[class='sign-in-button login-action hide-for-member']"
    LOC_SIGN_OUT_BUTTON_CSS = "[class*='logout-action']"
    LOC_LOG_IN_BUTTON_CSS = ".bBody"
    LOC_MENU_ICON_MAIN_CSS = "[class='help-menu-main image-settings ui-menu-item']"

    LOC_USERNAME_LOGIN_FIELD_XPATH = "//*[@id='input-1']"
    LOC_PASSWORD_LOGIN_FIELD_XPATH = '//*[@id="input-3"]'

    LOC_HELP_MENU_MAIN_XPATH = '//*[@id="ui-id-4"]'
    LOC_HELP_MENU_MAIN_CSS = "[id='ui-id-4']"
    LOC_HELP_MENU_LIST_XPATH = "/html/body/header/div[4]/ul/li/ul"
    LOC_SEARCH_CSS = "[class='js-search-button search-icon image-search']"
    LOC_INSECURE_FORM_CSS = "[class='insecure-form']"
    LOC_INSECURE_FORM_PROCEED_ID = "proceed-button"
    LOC_LOGIN_FAILED_CSS = ".login-failed > p:nth-child(3)"
    LOC_LOGIN_FAILED_SIGNINBTN_CSS = "[class='sign-in-link default-button']"

    # CableCo locators
    LOC_USERNAME_LOGIN_FIELD_CABLECO_XPATH = "//*[@id='username']"
    LOC_PASSWORD_LOGIN_FIELD_CABLECO_XPATH = '//*[@id="password"]'
    LOC_LOG_IN_BUTTON_CABLECO_CSS = ".default-button.mobileButn"

    LOC_MODIFY_ONEPASS_XPATH = "//button[contains(@class, 'js-modify-button')]"
    LOC_EDIT_BUTTON_CSS = "[class*='edit-button']"
    LOC_EMPTY_LIST_CSS = "[class='default-message todo-empty-list']"
    LOC_TO_DO_LIST_EDIT_BUTTON_CSS = "[class*='edit-button']"

    LOC_DELETE_BUTTON_CSS = "[class='default-button delete-button']"
    LOC_TO_DO_LIST_DELETE_BUTTON_CSS = "[class='default-button delete-button']"

    LOC_ELEMENT_IN_GUIDE_BY_XPATH = "//div[@data-channel-number][2]//ul[@class='shows']/li[1]"
    LOC_GUIDESHOW_XPATH_2 = "//div[@data-channel-number='4']//ul[@class='shows']/li[1]"

    LOC_GUIDE_CHANNEL_NUMBER = "data-channel-number"
    LOC_LOGO_CSS = ".image-mso-branding.hide-for-mobileos"

    LOC_WTW_SIGN_IN_GTS_XPATH = "//button[contains(text(),'Sign In to Get This Show')]"
    LOC_WTW_STRIPS = ".margin-left.feed-with-preview.js-feed-panel"
    LOC_WTW_STRIPS_XPATH = '//*[@id="main-content"]'

    LOC_EXIT_BANNER = "div.global-message:nth-child(4) > button:nth-child(2)"
