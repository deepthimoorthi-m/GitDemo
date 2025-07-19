import pytest
import re
from webportal.client_api.ondemand.locators import OnDemandLocators
from webportal.client_api.ondemand.labels import OnDemandLabels
from webportal.client_api.base.page import BasePage
from webportal.client_api.search.locators import SearchLocators


class OnDemandPage(BasePage):

    def go_to_OnDemand(self):
        self.driver.refresh()
        self.driver.clickElementByLinkText(OnDemandLabels.LBL_ON_DEMAND)
        self.driver.page_has_loaded()

    def go_to_Promotions(self):
        self.navigate_ondemand_submenu(OnDemandLabels.LBL_PROMOTIONS)

    def go_to_Movies_folder(self):
        self.log.info("I'm in verify_Movies method.")
        elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
        all_li = elem.find_elements_by_tag_name("li")
        for li in all_li:
            if OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5] in li.get_attribute("textContent") \
                    and li.text in OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5]:
                element = li.text
                self.log.info("text: {}  id: {}".format(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5], element))
                self.driver.clickElementByLinkText(OnDemandLabels.LBL_ON_DEMAND_SUBMENUS[5])
        self.driver.page_has_loaded(5)

    def navigate_ondemand_submenu(self, text):
        self.log.info("\nI'm in navigate_on_demand_submenu\n")
        elem = self.driver.getElementByXPath(OnDemandLocators.LOC_SUBMENU_XPATH)
        all_li = elem.find_elements_by_tag_name("li")
        for li in all_li:
            if text in li.get_attribute("textContent"):
                element = li.get_attribute("id")
                self.log.info("text: {}  id: {}".format(text, element))
                self.driver.clickElement(li)

    def click_on_All_Titles(self):
        self.driver.page_has_loaded()
        self.driver.clickElementByXPATH(OnDemandLocators.LOC_VALUEMOVIES_XPATH)

    def select_TVOD_Unencrypted_item(self):
        elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
        if elements is not None:
            movie_list = []
            for item in elements:
                all_movies = item.find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
                for movie in all_movies:
                    movie_name = movie.get_attribute("textContent")
                    self.log.info(f"Found TVOD unencrypted: {movie_name}")
                    movie_list.append(movie_name)
        else:
            self.log.info("There are not TVOD unencrypted asset")
            pytest.skip("There are not TVOD unencrypted asset")

        self.log.info("Unrated TVOD search")

        movie = None
        counter = 0
        while movie is None and counter < len(movie_list):
            self.driver.refresh()
            elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
            self.log.info("Try movie : {}".format(movie_list[counter]))
            all_movies = elements[0].find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
            all_movies[counter].click()
            self.driver.page_has_loaded()
            self.log.info("Successfully selected movie: {}".format(movie_list[counter]))
            self.log.info("Check that movie is unrated. If not, try another movie...")
            text = self.open_pop_up()
            if movie_list[counter] is not None and text is not None:
                movie = self.driver.getElementTextByCSS(OnDemandLocators.LOC_MOVIE_NAME_CSS)
                movie = re.sub(r"\(\d\d\d\d\)", '', movie)
                self.log.info("Movie searched is " + movie)
                return movie, text
            counter = counter + 1

    def open_pop_up(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_PLAY_BUTTON_CSS)
        pop_elem = self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
        if pop_elem is not None:
            div = pop_elem.find_element_by_css_selector(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
            text = div.text
            self.log.info(text)
            pattern = "for"
            if pattern in text:
                self.driver.clickElementByCSS(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
                self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
                return text
            else:
                self.log.info("Try other movie")
                try:
                    self.driver.clickElementByCSS(OnDemandLocators.LOC_CLOSE_POPUP_CSS)
                    self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
                except Exception:
                    self.driver.clickElementByXPATH(OnDemandLocators.LOC_CLOSE_PLAYER_XPATH)
                    self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS)
        else:
            self.log.info("Check all the movies and found no unrated TVOD asset")
        return None

    def cancel_pop_up(self):
        pop_up = self.driver.waitUntilElementIsDisplayedByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)
        button = pop_up.find_elements_by_css_selector(OnDemandLocators.LOC_POP_UP_WATCH_NOW_BTN_CSS)
        self.driver.clickElement(button[1])
        self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)

    def close_pop_up(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_CLOSE_CONFIRM_BTN_CSS)
        self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)

    def confirm_purchase(self):
        pop_up = self.driver.waitUntilElementIsDisplayedByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)
        button = pop_up.find_elements_by_css_selector(OnDemandLocators.LOC_POP_UP_WATCH_NOW_BTN_CSS)
        self.driver.clickElement(button[0])
        self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_POP_UP_CONFIRM_CSS)

    def click_movie(self):
        results = self.driver.getElementsByXPath(SearchLocators.LOC_SUGGESTED_LIST_TITLE_CABLECO_XPATH)
        self.driver.clickElement(results[0])
        self.driver.page_has_loaded()

    def click_watch_now_btn(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_PLAY_BUTTON_CSS)

    def click_pop_up_watch_now(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
        self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)

    def select_TVOD_Encrypted_item(self):
        elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
        if elements is not None:
            movie_list = []
            for item in elements:
                all_movies = item.find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
                for movie in all_movies:
                    movie_name = movie.get_attribute("textContent")
                    self.log.info(f"Found TVOD encrypted: {movie_name}")
                    movie_list.append(movie_name)
        else:
            self.log.info("There are not TVOD encrypted asset")
            pytest.skip("There are not TVOD encrypted asset")

        self.log.info("Rated TVOD search")

        movie = None
        counter = 0
        while movie is None and counter < len(movie_list):
            self.driver.refresh()
            elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
            self.log.info("Try movie : {}".format(movie_list[counter]))
            all_movies = elements[0].find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
            all_movies[counter].click()
            self.driver.page_has_loaded()
            self.log.info("Successfully selected movie: {}".format(movie_list[counter]))
            self.log.info("Check that movie is rated. If not, try another movie...")
            message = self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_INFO_CARD_MESSAGE_CSS)
            text = message.text
            if movie_list[counter] is not None and "Available until" in text:
                movie = self.driver.getElementTextByCSS(OnDemandLocators.LOC_MOVIE_NAME_CSS)
                movie = re.sub(r"\(\d\d\d\d\)", '', movie)
                self.log.info("Movie searched is " + movie)
            counter = counter + 1

    def web_player_playing_or_wn(self):
        try:
            self.log.info("check watch now pop-up")
            self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
            self.driver.clickElementByCSS(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
            self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS, 20)
            self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_PLAY_HEAD_CSS)
        except Exception:
            self.log.info("check web player")
            self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS, 20)
            self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_PLAY_HEAD_CSS)

    def close_web_player(self):
        self.driver.clickElementByXPATH(OnDemandLocators.LOC_CLOSE_PLAYER_XPATH)
        self.driver.waitUntilElementIsNotVisibleByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS)

    def resume(self):
        self.log.info("I'm in resume function")
        self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
        self.driver.clickElementByCSS(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
        self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WEB_PLAYER_CSS, 40)
        self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_PLAY_HEAD_CSS)

    def start_over(self):
        self.log.info("I'm in start over function")
        pop_elem = self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_WATCH_NOW_POPUP_CSS)
        div = pop_elem.find_elements_by_css_selector(OnDemandLocators.LOC_POP_UP_WATCH_NOW_CSS)
        for item in div:
            text = item.text
            if OnDemandLabels.LBL_START_OVER in text:
                self.driver.clickElement(item)

    def select_first_movie(self):
        elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
        if elements is not None:
            movie_list = []
            for item in elements:
                all_movies = item.find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
                for movie in all_movies:
                    movie_name = movie.get_attribute("textContent")
                    self.log.info(f"Found TVOD encrypted: {movie_name}")
                    movie_list.append(movie_name)
        else:
            self.log.info("There are not TVOD encrypted asset")
            pytest.skip("There are not TVOD encrypted asset")

        self.log.info("Preview button search")

        movie = None
        counter = 0
        while movie is None and counter < len(movie_list):
            self.driver.refresh()
            elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
            self.log.info("Try movie : {}".format(movie_list[counter]))
            all_movies = elements[0].find_elements_by_css_selector(OnDemandLocators.LOC_ALL_MOVIES_CSS)
            all_movies[counter].click()
            self.driver.page_has_loaded()
            self.log.info("Successfully selected movie: {}".format(movie_list[counter]))
            self.log.info("Check that Preview button is present. If not, try another movie...")
            btn = self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_Preview_BTN_CSS)
            if movie_list[counter] is not None and btn:
                movie = self.driver.getElementTextByCSS(OnDemandLocators.LOC_MOVIE_NAME_CSS)
                self.log.info("Movie searched is " + movie)
            counter = counter + 1

    def click_preview_btn(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_Preview_BTN_CSS)

    def go_to_TiVo_submenu(self):
        self.driver.clickElementByCSS(OnDemandLocators.LOC_TIVO_CSS)

    def click_on_Rating_folder(self):
        self.driver.page_has_loaded()
        self.driver.clickElementByXPATH(OnDemandLocators.LOC_RATING_FOLDER_XPATH)

    def select_IPVOD_item(self):
        elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
        if elements is not None:
            movie_list = []
            for item in elements:
                all_movies = item.find_elements_by_css_selector(OnDemandLocators.LOC_ALL_IPVOD_CSS)
                for movie in all_movies:
                    movie_name = movie.get_attribute("textContent")
                    self.log.info(f"Found IPVOD content: {movie_name}")
                    movie_list.append(movie_name)
        else:
            self.log.info("There are not IPVOD asset")
            pytest.skip("There are not IPVOD asset")

        self.log.info("IPVOD assets list")

        movie = None
        counter = 0
        while movie is None and counter < len(movie_list):
            self.driver.refresh()
            elements = self.driver.waitUntilElementsAreVisibleByXpath(OnDemandLocators.LOC_ON_DEMAND_GRID_XPATH)
            self.log.info("Try ipvod content : {}".format(movie_list[counter]))
            all_movies = elements[0].find_elements_by_css_selector(OnDemandLocators.LOC_ALL_IPVOD_CSS)
            all_movies[counter].click()
            self.driver.page_has_loaded()
            self.log.info("Successfully selected movie: {}".format(movie_list[counter]))
            self.log.info("Check that content is IPVOD...")
            message = self.driver.waitUntilElementIsVisibleByCSS(OnDemandLocators.LOC_INFO_CARD_MESSAGE_CSS)
            text = message.text
            if movie_list[counter] is not None and "Included in" in text:
                movie = self.driver.getElementTextByCSS(OnDemandLocators.LOC_MOVIE_NAME_CSS)
                movie = re.sub(r"\(\d\d\d\d\)", '', movie)
                self.log.info("Movie searched is " + movie)
            counter = counter + 1
