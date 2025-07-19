from webportal.client_api.base.locators import BaseLocators


class OnDemandLocators(BaseLocators):
    LOC_ON_DEMAND_TAB_CSS = "#menu-link-id-on-demand"
    LOC_MY_RENTALS_CSS = ".js-feed-title"
    LOC_SUBMENU_XPATH = "/html/body/header/div[2]/ul/li[2]/ul"
    LOC_FIRST_MOVIE_CSS = ".wtw-item.mov.is-selected"
    LOC_MOVIE_NAME_CSS = ".js-content-detail-link.link-primary"
    LOC_VALUEMOVIES_XPATH = "//*[@id='main-content']/div/div[5]/div[1]/ul/div/div/li[2]/div"
    LOC_ON_DEMAND_GRID_CSS = "div.js-feed-panel.wtw-grid"
    LOC_ON_DEMAND_GRID_XPATH = "//*[@id='main-content']/div[3]/div/div[2]/ul"
    LOC_ALL_TITLES_CSS = ".heading-container"
    LOC_PLAY_BUTTON_CSS = ".play-icon.fa-stack"
    LOC_WATCH_NOW_POPUP_CSS = ".popup-content"
    LOC_MOVIE_CSS = "#ui-id-27"
    LOC_CLOSE_POPUP_CSS = ".close.js-close.image-close"
    LOC_POP_UP_CONFIRM_CSS = ".purchase-dialog"
    LOC_CANCEL_BTN_XPATH = ".user-actions > button:nth-child(2)"
    LOC_CONFIRM_BTN_XPATH = ".user-actions > button:nth-child(1)"
    LOC_WEB_PLAYER_CSS = ".player-component.main-video"
    LOC_CLOSE_CONFIRM_BTN_CSS = ".ui-button-icon-primary.ui-icon.ui-icon-closethick"
    LOC_POP_UP_WATCH_NOW_CSS = ".watchnow-popup-item-container.vod"
    LOC_ALL_MOVIES_CSS = ".wtw-item.mov"
    LOC_POP_UP_WATCH_NOW_BTN_CSS = ".default-button"
    LOC_INFO_CARD_MESSAGE_CSS = ".js-entitlement-message.entitlement-message-container"
    LOC_PLAY_HEAD_CSS = ".playbar-container.js-playbar-container"
    LOC_CLOSE_WEB_PLAYER_BTN_CSS = ".js-close.close.rounded-background"
    LOC_PLAY_LABEL_CSS = "span.play-head-label.js-play-head-label"
    LOC_CLOSE_PLAYER_XPATH = "//div[@class='close-btn'] //button[@class='js-close close rounded-background']"
    LOC_WN_PLAY_CSS = ".watchnow-popup-item-text"
    LOC_Preview_BTN_CSS = ".js-preview-button.default-button.show-for-preview.hide-for-guest"
    LOC_TIVO_CSS = "#ui-id-24"
    LOC_RATING_FOLDER_XPATH = "//*[@id='main-content']/div/div[4]/div[1]/ul/div/div/li[1]/div"
    LOC_ALL_IPVOD_CSS = ".wtw-item.tv"
    LOC_MY_RENTALS_STRIP_XPATH = "//*[@id='main-content']/div[3]/div"
    LOC_MY_RENTALS_ACTIVE_XPATH = """//li[a[@id='menu-link-id-my-rentals']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_TV_NETWORKS_ACTIVE_XPATH = """//li[a[@id='menu-link-id-tv-networks']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_TV_NETWORK_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Bravo"
            or text()="CBS"
            or text()="ABC"]"""
    LOC_STRIP = "[class='items w2w-strip flickity-enabled is-draggable']"
    LOC_FEED = ".wtw-item"
    LOC_TV_SERIES_ACTIVE_XPATH = """//li[a[@id='menu-link-id-tv-series']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_TV_SERIES_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="All Series"
            or text()="Series G - M"
            or text()="Series N - S"]"""
    LOC_TiVo_ACTIVE_XPATH = """//li[a[@id='menu-link-id-tivo']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_TiVo_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="ByExpiration"
            or text()="SVOD"
            or text()="ByRating"]"""
    LOC_Armstrong_Neighborhood_ACTIVE_XPATH = """//li[a[@id='menu-link-id-armstrong-neighborhood']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Armstrong_Neighborhood_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Butler Co. PA"
            or text()="Mahoning Valley"
            or text()="Northwest PA"]"""
    LOC_Kids_ACTIVE_XPATH = """//li[a[@id='menu-link-id-kids']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Kids_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Cartoon Network"
            or text()="Disney Channel"
            or text()="Disney Junior"]"""
    LOC_Movies_ACTIVE_XPATH = """//li[a[@id='menu-link-id-movies']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Movies_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Free Studio Extras"
            or text()="New Releases"
            or text()="Featured Collections"]"""
    LOC_Free_Programs_ACTIVE_XPATH = """//li[a[@id='menu-link-id-free-programs']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Free_Programs_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Free Studio Extras"]"""
    LOC_All_Movies_ACTIVE_XPATH = """//li[a[@id='menu-link-id-all-movies']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_All_Movies_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="2 Day Rental"
            or text()="Drama"
            or text()="Show All Titles"]"""
    LOC_HD_On_Demand_ACTIVE_XPATH = """//li[a[@id='menu-link-id-hd-on-demand']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_HD_On_Demand_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="All Movies"
            or text()="New Releases"]"""
    LOC_Promotions_ACTIVE_XPATH = """//li[a[@id='menu-link-id-promotions']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Promotions_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Indie Spotlight"
            or text()="Earth Day"]"""
    LOC_New_Releases_ACTIVE_XPATH = """//li[a[@id='menu-link-id-new-releases']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_New_Releases_STRIPS = """//div[@id='main-content']//h3[text()="New Releases"]"""
    LOC_Adult_On_Demand_ACTIVE_XPATH = """//li[a[@id='menu-link-id-adult-on-demand']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Adult_On_Demand_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="By Category"
            or text()="DigitalPlayground "
            or text()="Show All Titles"]"""
    LOC_Events_On_Demand_ACTIVE_XPATH = """//li[a[@id='menu-link-id-events-on-demand']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Events_On_Demand_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Specials"]"""
    LOC_Premium_TV_ACTIVE_XPATH = """//li[a[@id='menu-link-id-premium-tv']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_Premium_TV_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Showtime"
            or text()="HBO"]"""
    LOC_QE_ACTIVE_XPATH = """//li[a[@id='menu-link-id-qe']
            and contains(concat(' ', normalize-space(@class), ' '), ' active ')]"""
    LOC_QE_STRIPS = """//div[@class='js-linked-gallery-container']//h3[text()="Experiments"]"""
