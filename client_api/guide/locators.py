# -*- coding: utf-8 -*-
from webportal.client_api.base.locators import BaseLocators


class GuideLocators(BaseLocators):
    LOC_GUIDE_TAB_CSS = "#menu-link-id-guide"
    LOC_GUIDE_XPATH = "//a[@id='menu-link-id-guide']"
    LOC_GUIDE_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and contains(@aria-labelledby, 'menu-link-id-guide')]"
    LOC_GUIDELIST = "guide-listing"
    LOC_GUIDE_FILTER_CSS = ".header-cell-left .ui-selectmenu-text"
    LOC_GUIDE_ALLCHANNELS_XPATH = "html/body/div[2]/div/div/div/div/div[1]/form/div/div[1]/div[1]/div/ul/li[1]"
    LOC_GUIDE_NOW_CSS = "span.time-jump-item.jump-to-now.guide-button.default-button"
    LOC_GET_THIS_SHOW_OR_EPISODE_BUTTON_CSS = ".js-get-button.default-button.show-for-get.hide-for-guest"
    LOC_SCHEDULE_THIS_SHOW_OR_EPISODE_BUTTON_CSS = "button.default-button.record-content-button"
    LOC_LIVETV_XPATH = "//div[contains(text(),'Live TV')]"
    LOC_MY_RECORDING_XPATH = "//div[@class='watchnow-popup-item-container'] //div[@class='watchnow-popup-item-text' " \
                             "and contains(text(),'My Recording')] "
    LOC_NOTIFICATION_MSG_CSS = "[class='notification-message']"
    LOC_GET_THIS_SHOW_BUTTON = "button.js-signin-button.default-button.hide-for-member"
    LOC_RECORD_THIS_EPISODE_BUTTON_CSS = "[class*='record-episode-button']"
    LOC_RECORD_THIS_SHOW_BUTTON_CSS = "[class='dropdown-button record-show-button hide-for-cant-record']"
    LOC_EPISODE_RECORD_WITH_THIS_OPTIONS_BUTTON = ".default-button.record-episode-button"
    LOC_SHOW_RECORD_WITH_THIS_OPTIONS_BUTTON = ".default-button.record-show-button"
    LOC_MY_SHOWS_TAB_CSS = "#menu-link-id-my-shows"
    LOC_WATCHNOW = ".watch-now-button.default-button.play-btn.text-primary-contrast"
    LOC_CONFIRMATION_WATCHNOW = "//*[@class='getfrom-line getfrom-has-transcoder']/button"
    LOC_PLAYING_SHOW_CSS = "div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.popup-player.tivo_live"
    LOC_PLAYING_SHOW_FROM_POPUP_CSS = "[class='watchnow-popup-item-text']"
    LOC_PLAYING_SHOW_POPUP_TITLE = "[class='popup-title']"
    LOC_WATCHNOW_CSS = ".play-icon.fa-stack"
    LOC_RECORDING_CONFIRMATION_POPUP_XPATH = "html/body/div[5]/div[1]/span"
    LOC_RECORDED_ASSET = "html/body/div[5]/div[2]/div[1]/div[2]/div[1]/h3/span[2]/span[1]"
    LOC_GUIDE_GRID_CSS = "div.js-guide-content.programs"
    LOC_GUIDE_LINK_TEXT = "GUIDE"
    LOC_GUIDESHOW_XPATH = "//div[@data-channel-number='3']//ul[@class='shows']/li[1]"
    LOC_GUIDEWATCHNOW_XPATH = "//div[@class='watchnow-popup-item-text'][contains(text(),'Live TV')]"
    LOC_GUIDEWATCH_XPATH = "//div[@class='video-source-button-text']"  # 'Live TV' icon under 'Play' icon
    LOC_GUIDEWATCH_CSS = "[class='video-source-button-text']"
    LOC_SIGNOUT_LINK_TEXT = "Sign out"
    LOC_RECORDED_ASSET_CSS = ".js-content-detail-link.link-primary"
    LOC_LIVETV_CLOSE = "button.ui-button.ui-widget.ui-state-default." \
                       "ui-corner-all.ui-button-icon-only.ui-title-dialog-titlebar-close.firefinder-match"
    LOC_ABB_EPISODE = "div.js-guide-cell.show-season-episode"
    LOC_RECORDING_ICON = "span.js-signal-strength.signal-strength.strongest"
    LOC_GOOGLE_FORM = "/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"
    LOC_GOOGLE_FORM_CSS = ".gLFyf"
    LOC_GOOGLE_LOGO = "html/body/div[3]/form/div[2]/div[1]/div[1]/a/img"
    LOC_MAIN_PAGE_SETTING = "#ui-id-4"
    LOC_ZIP_CODE = "//input[@placeholder='Enter Zip Code']"
    LOC_SHOWS_POSTER_XPATH = "(//ul[@class='shows']//span)[6]"
    LOC_ZIP_CODE_LINE_UP_XPATH = "(//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']//li)[2]"
    LOC_GTS_BUTTON = "//button[@class='js-signin-button default-button hide-for-member']"
    LOC_GUIDE_LIST_CSS = "#guide-listing"
    LOC_GUIDE_CONTENT = "//div[@class='js-guide-content programs']"
    LOC_CAST = "//a[contains(text(),'Cast')]"
    LOC_WISHLIST_BUTTON = "//span[@class='person-wishlist-text']"
    LOC_ACTOR = "(//div[@class='flickity-slider']//li[@class='person is-selected'])[1]"
    LOC_WISHLIST_POP_UP = "//div[contains(text(),'Your WishList has been created')]"
    LOC_CAST_NOT_FOUND = "//div[@class='cast-no-cast-message']"
    LOC_GUIDE_GRID = "(//div[@class='js-guide-cell'])[1]"
    LOC_RECORDED_WHISPER_CSS = ".whisper-notification"
    CLOSE_WINDOW_SCREEN_XPATH = "//div[@class='close-btn'] //button[@class='js-close close rounded-background']"
    LOC_ELEMENT_IN_GUIDE_XPATH_2 = "//div[@data-channel-number='5']//ul[@class='shows']/li[1]"
    CLOSE_WINDOW_POPUP_XPATH = "//div[contains(@style, 'display: block')]//span[contains(@class, 'closethick')]"
    LOC_RECORD_ICON_CSS = "span.showing-info-status-icon.icon-tool-tip.image-recording-now"
    LOC_RECORD_ICON_FROM_TITLE_CSS = "span.onepass-status.js-status-icon.icon-tool-tip.image-recording-now"
    LOC_RECORDED_PLAYER_SCREEN_CSS = "div.player-component.main-video"
    CLOSE_ELEMENT_WINDOW_XPATH = "//div[contains(@style, 'display: block')]//button[contains(@class, 'js-close')]"
    LOC_EPISODE_NAME_CSS = ".episode-name"
    LOC_EPISODE_NUMBER_CSS = ".js-season-episode.season-in-title.season-info"
    LOC_RECORD_WHISPER_CSS = ".whisper-notification"
    LOC_AIRING_NOW_CSS = "[class='play-icon fa-stack']"
    LOC_RECORDED_ASSET_CSS_1 = "span.episode-name"
    LOC_GUIDE_GRID_CELL_CSS = ".guide-grid"
    LOC_CHANNEL_LIST_UNLOCKED = "[class='channel channel-unlocked']"

    # Cableco locators
    LOC_PLAYING_SHOW_CABLECO_CSS = ".player-component.main-video"
    LOC_GUIDE_NEW_FEATURE_CSS = ".dialog-body.ui-dialog-content.ui-widget-content"
    LOC_GUIDE_OK_CSS = ".user-actions"
