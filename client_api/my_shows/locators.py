# -*- coding: utf-8 -*-
from webportal.client_api.base.locators import BaseLocators


class MyShowsLocators(BaseLocators):

    LOC_MY_SHOWS_TAB_CSS = "#menu-link-id-my-shows"
    LOC_MY_SHOWS_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and contains(@aria-labelledby," \
                                     " 'menu-link-id-my-shows')]"
    LOC_MOVIES = "#menu-link-id-movies"
    LOC_EDIT_BUTTON_XPATH = "//*[@id='one-pass-list']/ul/li[2]/div/div[2]/div/span[1]/button"
    LOC_FIRSTELEMENT_CSS = "li[class*='onepass-line onepass']"
    # LOC_SECONDELEMENT_XPATH = "//ul[@class='js-one-pass-list ui-selectable']/li[2]/div[
    # @class='line-item-body']/span[@class='js-title onepass-title']"
    LOC_SECONDELEMENT_XPATH = "//ul[@class='js-one-pass-list ui-selectable']/li[2]/div[@class='line-item-body']" \
                              "/div/span[@class='ellipses-truncated-text']"
    LOC_MYSHOWS_CHECKBOX_CSS = ".all-episodes-item.episode-item.movie.is-selected"
    LOC_DELETE_BUTTON_XPATH = "//*[@id='one-pass-list']/ul/li[2]/div/div[2]/div/span[2]/button[1]"
    # TO DO: I belive we need to refactor the code.
    # This is not an apropiate solution for this case (Delete a reorded show from My Shows)
    LOC_DELETE_CONFIRM_XPATH = "html/body/div[3]/div[2]/div[2]/ul/li[1]/button"
    LOC_MYSHOWSLIST = "one-pass-list"
    LOC_MYSHOWSLIST_XPATH = "//ul[contains(@aria-controls, 'one-pass-list')]"
    LOC_ELEMENT_IN_QUICKONEPASS_CSS = ".tv"
    LOC_DELETE_CONFIRM_CSS = ".delete-remove-onepass-button.default-button.submit-button"
    LOC_DELETE_CONFIRM_MOVIE_CSS = ".delete-show-btn.default-button.submit-button.confirmation-button"
    LOC_DELETEEVERYTHING_CONFIRM_CSS = ".delete-contents-button.default-button.submit-button"
    LOC_DELETE_CONFIRM_STREAMING_CSS = ".delete-streaming-button.default-button.submit-button"
    LOC_DELETE_RECORDING_CONFIRM_CSS = ".delete-recording-button.default-button.submit-button"
    LOC_SHOW_ITEM_TITLE_CSS = ".episode-title.js-link"
    xpath = "//*[@id='one-pass-list']/ul/li[2]/div/div[3]/ul/div/div/li[1]/div[4]/a"
    LOC_SHOW_ITEM_LIST_CSS = ".all-episodes-item.episode-item.movie.is-selected"
    LOC_STREAMING_MOVIES = ".onepass-line.onepass-folder-line.is-all-shows.is-my-shows-folder.is-movies"

    LOC_DELETE_POPUP_CSS = ".ui-dialog"
    LOC_MY_SHOW_SHOWS_CONTAINER_CSS = ".js-one-pass-list"
    LOC_SHOW_ITEM_IMAGE = ".img-container"
    LOC_GET_SHOW = ".show-for-get"
    LOC_BOOKMARK = ".image-source-bookmark"
    LOC_DELETE_SHOW = ".show-for-delete"
    LOC_DROP_DOWN_GET_SHOW = ".add-season-streaming-button"
    LOC_BOOKMARK_MOVIE = ".dropdown-button.add-streaming-video-button"
    LOC_FIRST_MOVIE_CSS = ".wtw-item.mov.is-selected"
    LOC_MOVIE_NAME = ".js-content-detail-link.link-primary"
    LOC_WTW_GET_THIS_SHOW_XPATH = "//div[@class='siteforceSldsOneColLayout siteforceContentArea']"
    LOC_MY_SHOW_SIGN_IN_BUTTON_CSS = "[class='default-button login-action']"
    LOC_MY_SHOW_WMD_XPATH = "//p[@class='default-message']"
    LOC_MY_SHOWS_LIST = "#one-pass-list"
    LOC_ALL_SHOWS_MENU = "//li[@id='ui-id-76']"
    LOC_ALL_SHOWS = "//li[@id='ui-id-84']"
    LOC_MY_SHOW_WISHLIST = "//div[@class='line-item-body']//span[@class='onepass-status js-status-icon " \
                           "icon-tool-tip image-folder-wishlist']"
    LOC_EDIT = "//div[@class='carousel-edit-selectors']//span"
    LOC_CHECK_BOX = "(//div[@class='image-checkbox edit-checkbox'])[1]"
    LOC_DELETE = "//button[@class='default-button delete-button']"
    LOC_BOX_NAME = "//div[contains(text(),'Bolt 3')]"
    LOC_SETTING_ICON = "//li[@class='help-menu-main image-settings ui-menu-item']"
    LOC_SHOW_ITEM_LISTS_CSS = ".onepass-line:not(.recently-deleted-recordings-folder):not(.is-movies):not(" \
                              ".is-suggestions):not(.not-currently-available-folder)"
    LOC_RECORDED_WHISPER_CSS = ".whisper-notification"
    LOC_BOOKMARK_MOVIE_CSS = "[class='button-icon image-source-bookmark']"

    # Cableco
    LOC_STREAMING_CABLECO_MOVIES_CSS = ".onepass-line.onepass-folder-line.is-all-shows.is-my-shows-folder.is-tv-series" \
                                       ":not(.recently-deleted-recordings-folder)"
