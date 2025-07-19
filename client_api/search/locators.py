from webportal.client_api.base.locators import BaseLocators


class SearchLocators(BaseLocators):
    LOC_TEXT_FIELD_XPATH = "//input[@placeholder='Search Shows, People, Channels']"
    LOC_SUGGESTED_LIST_TITLE_CSS = "[id='ui-id-8']"
    LOC_SUGGESTED_LIST_PERSON_CSS = "[class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']"
    LOC_SUGGESTED_LIST_PERSON_POSTER_CSS = ".js-person-image.img-container"
    LOC_SUGGESTED_LIST_ROLES_XPATH = "//li[@class='ui-widget-content ui-menu-item']//p[contains(@class," \
                                     " 'person-roles')]"
    LOC_SUGGESTED_LIST_ROLES_CSS = ".js-person-roles.people-detail"
    LOC_SUGGESTED_LIST_POSTER_XPATH = "//ul[@id='ui-id-8']//div[contains(@class, 'loaded-image') or contains(@class, " \
                                      "'is-fallback-image')]"
    LOC_SUGGESTED_LIST_YEAR_XPATH = "//ul[@id='ui-id-8']//div[contains(@class, 'content-title')]/span[2]"
    LOC_SUGGESTED_LIST_RATING_XPATH = "//ul[@id='ui-id-8']//div[contains(@class, 'js-rating')]"
    LOC_SUGGESTED_LIST_GENRE_XPATH = "//ul[@id='ui-id-8']//div[contains(@class, 'genre')]"
    LOC_AUTO_SUGGEST_XPATH = "//ul[@id='ui-id-8']"
    LOC_MENU_ICON_MAIN_CSS = ".help-menu-main"
    LOC_CLOSE_BUTTON_CSS = ".js-search-button.search-icon.image-search.close-btn"
    LOC_AUTO_SEARCH_LIST_CSS = ".ul#ui-id-8.ui-autocomplete.ui-front.ui-menu.ui-widget.ui-widget-content"

    LOC_SUGGESTED_LIST_SHOW_XPATH = "//ul[@id='ui-id-8']//li/descendant::div[@class='js-title content-title']/span[1]"
    LOC_SUGGESTED_LIST_EPISODE_NAME_XPATH = "//ul[@id='ui-id-8']//span[contains(@class, 'episode-name')]"
    LOC_SUGGESTED_LIST_PERSON_NAME_XPATH = "//li[@class='ui-widget-content ui-menu-item']" \
                                           "//span[@class='highlight-text']"
    LOC_SUGGESTED_LIST_SPORT_XPATH = "//li[@class='ui-widget-content ui-menu-item']//span[@class='highlight-text']"

    # Cableco Locators
    LOC_AUTO_SUGGEST_CABLECO_XPATH = "//ul[@id='ui-id-8']"
    LOC_SUGGESTED_LIST_TITLE_CABLECO_XPATH = "//ul[@id='ui-id-8']//li/descendant::div[@class='js-title content-title']"
    LOC_ALL_EPISODES_STRIP_XPATH = "//*[@id='main-content']/div/div[3]/div[1]/div/div[3]/ul/div/div"
    LOC_LIST_EPISODIC_NAMES_CSS = ".sub-title.remove-bottom-margin"
