from webportal.client_api.my_shows.locators import MyShowsLocators
from webportal.client_api.my_shows.labels import MyShowsLabels
from webportal.client_api.base.page import BasePage


class MyShowsPage(BasePage):

    def go_to_MyShows(self):
        self.driver.refresh()
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MY_SHOWS_TAB_CSS)
        self.driver.clickElementByLinkText(MyShowsLabels.LBL_MYSHOWS)
        self.driver.waitUntilElementIsDisplayedByXpath(MyShowsLocators.LOC_MYSHOWSLIST_XPATH)

    def go_to_Movies(self):
        self.driver.waitUntilElementIsDisplayedByCSS(MyShowsLocators.LOC_MENU_ICON_MAIN_CSS)
        self.driver.clickElementByLinkText(MyShowsLabels.LBL_WHATTOWATCH)
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MOVIES)
        self.driver.clickElementByCSS(MyShowsLocators.LOC_MOVIES)

    def search_movie_and_select(self):
        self.driver.page_has_loaded()
        self.driver.clickElementByCSS(MyShowsLocators.LOC_FIRST_MOVIE_CSS)
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MOVIE_NAME)
        return self.driver.getElementTextByCSS(MyShowsLocators.LOC_MOVIE_NAME)

    def create_bookmark(self):
        self.driver.clickElementByCSS(MyShowsLocators.LOC_GET_SHOW)
        self.driver.clickElementByCSS(MyShowsLocators.LOC_BOOKMARK_MOVIE_CSS)
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETE_SHOW)
        self.driver.waitUntilElementIsNotVisibleByCSS(MyShowsLocators.LOC_RECORDED_WHISPER_CSS)

    def delete_movie(self, movie):
        myShowTitleList = self.getShowsTitleList()
        for movie_check in myShowTitleList:
            self.log.info(movie_check)
            end_film = "..."
            if end_film in movie_check:
                movie_check = movie_check.replace(end_film, '')
                self.log.info(movie_check)
            if movie_check in movie:
                self.log.info(f"== Movie '{movie}' was found. Proceed for deletion. ==")
                self.deleteShow()
                return

    def getShowsTitleList(self):
        self.log.info("### I'm in getShowsTitleList() method. ###")
        self.driver.refresh()
        self.log.info("== Select Folder 'Streaming Movies' ==")
        self.driver.clickElementByCSS(MyShowsLocators.LOC_STREAMING_MOVIES)
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MYSHOWS_CHECKBOX_CSS)
        myShowsList = self.driver.getElementsByCSS(MyShowsLocators.LOC_SHOW_ITEM_LIST_CSS)
        myShowsTitleList = list()
        for show in myShowsList:
            myShowsTitleList.append(
                self.driver.getElementFromParentByCSS(show, MyShowsLocators.LOC_SHOW_ITEM_TITLE_CSS).text)
        return myShowsTitleList

    def deleteShow(self):
        self.log.info("### I'm in deleteShow() method. ###")
        self.driver.clickElementByXPATH(MyShowsLocators.LOC_EDIT_BUTTON_XPATH)
        self.driver.clickElementByCSS(MyShowsLocators.LOC_MYSHOWS_CHECKBOX_CSS)
        self.driver.clickElementByXPATH(MyShowsLocators.LOC_DELETE_BUTTON_XPATH)
        try:
            self.log.info("== Confirm deletion of the show ==")
            self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETE_CONFIRM_MOVIE_CSS)
            self.log.info("== The show was successfully deleted ==")
        except Exception:
            pass

    def go_to_My_Shows(self):
        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_MY_SHOWS_TAB_CSS)
        self.driver.clickElementByLinkText(MyShowsLabels.LBL_MYSHOWS)
        self.driver.waitUntilElementIsDisplayedByCSS(MyShowsLocators.LOC_EDIT_BUTTON_CSS)

    def delete_All_From_MyShows(self):
        my_shows_List = self.driver.getElementsByCSS(MyShowsLocators.LOC_SHOW_ITEM_LISTS_CSS)
        try:
            self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_EDIT_BUTTON_CSS)
            self.driver.clickElementByCSS(MyShowsLocators.LOC_EDIT_BUTTON_CSS)
            show_list = []
            for show in my_shows_List:
                show_list.append(show.text)
                show.click()
            self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETE_BUTTON_CSS)
            self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETE_BUTTON_CSS)
            try:
                self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETEEVERYTHING_CONFIRM_CSS)
                self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETEEVERYTHING_CONFIRM_CSS)
                self.log.info(f"Shows Deleted Successfully: {show_list}")
                self.driver.refresh()
            except Exception:
                try:
                    self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETE_RECORDING_CONFIRM_CSS)
                    self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETE_RECORDING_CONFIRM_CSS)
                    self.log.info(f"Shows Deleted Successfully: {show_list}")
                    self.driver.refresh()
                except Exception:
                    try:
                        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETE_CONFIRM_STREAMING_CSS)
                        self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETE_CONFIRM_STREAMING_CSS)
                        self.log.info(f"Shows Deleted Successfully: {show_list}")
                        self.driver.refresh()
                    except Exception:
                        self.driver.waitUntilElementIsClickableByCSS(MyShowsLocators.LOC_DELETE_CONFIRM_CSS)
                        self.driver.clickElementByCSS(MyShowsLocators.LOC_DELETE_CONFIRM_CSS)
                        self.log.info(f"Shows Deleted Successfully: {show_list}")
                        self.driver.refresh()
        except Exception:
            self.log.info("List is empty and Nothing to delete from My-Shows")
