# -*- coding: utf-8 -*-
from webportal.client_api.base.locators import BaseLocators


class WhatToWatchLocators(BaseLocators):

    LOC_COLAPSED_NAV_MENU_CSS = ".mobile-main-nav-menu-main"
    LOC_WHAT_TO_WATCH_CSS = "[id = 'menu-link-id-what-to-watch']"
    LOC_MYSHOWS_CSS = "[id='menu-link-id-my-shows']"
    LOC_NEWLY_AVAILABLE_TEXT_CSS = ".tveStartFeed1 .feed-title"
    LOC_LIVE_TV_CHANNELS_CSS = ".tveStartFeed6 .feed-title"
    LOC_MY_SHOWS_CSS = ".tveStartFeed4 .feed-title"
    LOC_POPULAR_CSS = ".tveStartFeed3Tv .feed-title"
    LOC_RECOMMENDATIONS_CSS = ".tveStartFeed2 .feed-title"
    LOC_BROWSE_CATEGORIES_CSS = ".tveStartFeed5Tv .feed-title"
    LOC_WTW_NEWLY_AVAILABLE_INFO_CSS = ".show-info"  # this locator must be relative to a item from the Newly Available feed
    LOC_WTW_NEWLY_AVAILABLE_TILE_CSS = ".info-overlay"  # this locator must be relative to a item from the Newly Available feed
    LOC_SHOWINFO_POPUP_EPISODENAME_CSS = ".ellipses-truncated-text"
    LOC_MSOBRANDING_IMAGE_XPATH = "//a[@class='image-mso-branding']"
    LOC_MSOBRANDING_IMAGE_CSS = ".image-mso-branding"
    LOC_HOMELINK_CSS = ".top-nav-link.top-nav-home-link"
    LOC_SEARCH_XPATH = "html/body/header/div[2]/div[2]/div/input"
    LOC_HOMELINK_XPATH = ".top-nav-home-link a"
    LOC_WTW_ON_TV_TODAY_TEXT = "On TV Today"
    LOC_WTW_ON_TV_TODAY_TILE_XPATH = "/html/body/div[2]/div/div[2]/div[1]/ul/div/div/li[1]/div/div[1]"
    LOC_WTW_ON_TV_TODAY_TILE_CSS = "[class='js-program-image program-image wtw-feed-image tv']"

    LOC_WTW_ONTV_ICON_CSS = "[class='broadcast-status-icon icon-tool-tip image-tv']"

    LOC_WTW_ON_TV_TODAY_ASSET_XPATH = "//h2[@class = 'main-title']"
    # LOC_WTW_GET_THIS_SHOW_BUTTON_CSS = "[class='js-get-button default-button show-for-get hide-for-guest']"
    LOC_WTW_GET_THIS_SHOW_BUTTON_CSS = ".js-get-button.default-button.show-for-get.hide-for-guest"
    LOC_WTW_SHOW_SHARE_XPATH = "//span[@class='js-share image-class image-share']"
    LOC_WTW_SHOW_SHARE_CSS = ".js-share.image-class.image-share"
    LOC_WTW_SHOW_SHARE_TITLE_XPATH = "//div[contains(@class, 'share-this-show')]"
    LOC_WTW_SHOW_SHARE_FACEBOOK_XPATH = "//i[contains(@class, 'facebook')]"
    LOC_WTW_SHOW_SHARE_TWITTER_XPATH = "//i[contains(@class, 'twitter')]"
    LOC_WTW_SHOW_SHARE_EMAIL_XPATH = "//i[contains(@class, 'envelope')]"
    LOC_WTW_SHOW_SHARE_FACEBOOK_CSS = ".jssocials-share.jssocials-share-facebook"
    LOC_WTW_SHOW_SHARE_TWITTER_CSS = ".jssocials-share.jssocials-share-twitter"
    LOC_WTW_SHOW_SHARE_EMAIL_URL_CSS = ".jssocials-share.jssocials-share-email"
    LOC_WTW_GET_THIS_SHOW_WINDOW_CSS = "[class='ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix']"
    LOC_CREATE_ONEPASS_OPTION_CSS = "[class='dropdown-button get-onepass-button']"
    LOC_WTW_ONEPASS_EDIT_WINDOW_CSS = "[class='ui-dialog-title']"
    LOC_CREATE_ONEPASS_BUTTON_CSS = '[class*="submit-button"]'
    LOC_CREATE_ONEPASS_WHISPER_CSS = ".whisper-notification"
    LOC_MODIFY_ONEPASS_CSS = "[class='js-modify-button default-button show-for-modify hide-for-guest']"
    LOC_CANCEL_ONEPASS_OPTION_XPATH = ".//*[@data-action='cancelOnePassAction']"
    LOC_CANCEL_ONEPASS_CONFIRM_XPATH = ".//*[@data-event='cancelOnePass']"
    LOC_ASSET_NAME_XPATH = "//span[contains(@class, 'js-content')]"
    LOC_ASSET_NAME_CSS = "[class='js-content-detail-link link-primary']"
    LOC_ASSET_SEASON_EPISODE_XPATH = "//span[contains(@class, 'js-season-episode')]"
    LOC_ASSET_SEASON_EPISODE_CSS = "[class='js-season-episode season-in-title season-info']"
    LOC_ASSET_EPISODE_NAME_XPATH = "//span[contains(@class, 'episode-name')]"
    LOC_ASSET_EPISODE_NAME_CSS = "[class='episode-name']"
    LOC_SUB_MENU_NAVIGATION_CSS = ".link-primary"
    LOC_WTW_ON_TV_TODAY_XPATH = "//a[@id='menu-link-id-on-tv-today']"
    LOC_WTW_VIEW_ALL_XPATH = "(//div[@class='js-linked-gallery-container']//h5)[1]"
    LOC_WTW_CONTENT_STRIP_XPATH = "//ul[@class='items']//li"
    LOC_WTW_POSTER_CONTENT_XPATH = "(//ul[@class='items']//li)[1]"
    LOC_MY_SHOW_WMD_XPATH = "//p[@class='default-message']"
    LOC_MY_SHOW_SIGN_IN_BUTTON_XPATH = "//div[@class='action-button']"
    LOC_MY_SHOWS_XPATH = "//a[@id='menu-link-id-my-shows']"
    LOC_WTW_GET_THIS_SHOW_XPATH = "//div[@class='siteforceSldsOneColLayout siteforceContentArea']"
    LOC_BOX_SELECTION_XPATH = "//li[@class='help-menu-main image-settings ui-menu-item']"
    LOC_WTW_HIGHLIGHT_CSS = "[class='main-nav-item menu-has-submenus ui-menu-item active']"
    LOC_WTW_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and contains(@aria-labelledby," \
                                " 'menu-link-id-what-to-watch')]"
    LOC_WTW_NAV_MENU_XPATH = "//ul[contains(@id, 'ui-id-1')]"
    LOC_WTW_NAV_SUBMENU_XPATH = "//ul[contains(@style, 'display: block')]"
    LOC_WTW_HIGHLIGHT = "//li[@class='sub-nav-item js-link ui-menu-item active ui-state-hover is-selected']//span"
    LOC_WTW_HIGH_CSS = "sub-nav-item.js-link.ui-menu-item.active"
    LOC_JUST_FOR_ME = "#menu-link-id-just-for-me"
    LOC_JUST_FOR_ME_HIGHLIGHTED_XPATH = "//li[contains(@class, 'active')and contains(@aria-labelledby," \
                                        " 'menu-link-id-just-for-me')]"
    LOC_ON_TV_TODAY_STRIP_NAME_XPATH = "//h3[contains(text(), 'On TV Today')]"
    LOC_WTW_ON_TV_TODAY = "#menu-link-id-on-tv-today"
    LOC_SPORTS = "#menu-link-id-sports"
    LOC_MOVIES = "#menu-link-id-movies"
    LOC_TV_SERIES = "#menu-link-id-tv-series"
    LOC_KIDS = "#menu-link-id-kids"
    LOC_COLLECTIONS = "#menu-link-id-collections"
    LOC_BOX_SETS = "#menu-link-id-box-sets"
    LOC_VIEW_ALL_XPATH = "//div[contains(@class,'ui-helper-clearfix')]/h5"
    LOC_STRIP_ELEMENT = ".js-linked-gallery-container"
    LOC_VIEW_ALL_ITEMS = ".items"
    LOC_VIEW_ALL_FIRST_ITEM = ".wtw-item.tv"
    LOC_JUS_FOR_ME_ACTIVE = """//li[a[@id='menu-link-id-just-for-me']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_JUST_FOR_ME_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="On TV Today"
            or text()="Sports"
            or text()="Movies"
            or text()="TV Series"
            or text()="Kids"]"""

    LOC_ON_TV_TODAY_ACTIVE = """//li[a[@id='menu-link-id-on-tv-today']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_ON_TV_TODAY_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="TV Shows on Now"
            or text()="Sports on Now"
            or text()="Movies on Now"
            or text()="TV Shows on Later"
            or text()="Sports on Later"
            or text()="Movies on Later"]"""

    LOC_SPORTS_ACTIVE = """//li[a[@id='menu-link-id-sports']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_SPORTS_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()='Sports on Now'
            or text()='Sports on Later'
            or text()='NFL Football'
            or text()='College Football'
            or text()='NBA Basketball'
            or text()='Soccer'
            or text()='Sports Talk'
            or text()='Other Sports']"""

    LOC_MOVIES_ACTIVE = """//li[a[@id='menu-link-id-movies']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_MOVIES_STRIPS = """//div[@class='js-linked-gallery-container']//h3[
            text()='4-Star Movies This Week'
            or text()='Action'
            or text()='Animation'
            or text()='Comedy'
            or text()='Documentary'
            or text()='Drama'
            or text()='Romance'
            or text()='Sci-Fi & Fantasy']"""
    LOC_FEED = ".wtw-item"
    LOC_STRIP = "[class='items w2w-strip flickity-enabled is-draggable']"

    LOC_TV_SERIES_ACTIVE = """//li[a[@id='menu-link-id-tv-series']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_TV_SERIES_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()='New Shows'
            or text()='Season Premieres'
            or text()='Now Available to Stream'
            or text()='Sitcoms'
            or text()='Crime Dramas'
            or text()='Comedy'
            or text()='Drama'
            or text()='Game Shows']"""

    LOC_KIDS_ACTIVE = """//li[a[@id='menu-link-id-kids']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_KIDS_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()='Kids Shows on Now'
            or text()='Kids & Family Movies'
            or text()='Kids Musicals'
            or text()='Kids TV-Y'
            or text()='Kids TV-Y7'
            or text()='Educational TV for Kids'
            or text()='Educational TV for Teens']"""

    LOC_COLLECTIONS_ACTIVE = """//li[a[@id='menu-link-id-collections']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_COLLECTIONS_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Only '90s Kids Will Remember"
            or text()="Live Laugh Love"
            or text()="Tick Tock"
            or text()="Buzzfeed's Most Rewatchable Movies"
            or text()="Feel-Good Movies"
            or text()="This Year's Oscar Winners"
            or text()="Best Comedy Movies  of the Decade"
            or text()="Best Comedy TV of The Decade"]"""

    LOC_BOX_SETS_ACTIVE = """//li[a[@id='menu-link-id-box-sets']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_BOX_SETS_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Only 'American Pie Box Set"
            or text()="Austin Powers Box Set"
            or text()="Back to the Future Box Set"
            or text()="Batman Box Set"
            or text()="Blade Box Set"
            or text()="Bring It On Box Set"
            or text()="Clint Eastwood Box Set"
            or text()="DC Movie Box Set"]"""

    LOC_WTW_SHARE_FACEBOOK_PAGE_XPATH = "//h2[@id='homelink']"
    LOC_WTW_SHARE_TWITTER_PAGE_XPATH = "//div[@class='css-1dbjc4n r-18u37iz']"
