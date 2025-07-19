from webportal.client_api.guide.conftest import *
from webportal.client_api.what_to_watch.conftest import *
from webportal.client_api.my_shows.conftest import *
from webportal.client_api.manage.conftest import *
from webportal.client_api.ondemand.conftest import *


@pytest.mark.usefixtures("setup_my_shows")
@pytest.mark.usefixtures("setup_what_to_watch")
@pytest.mark.usefixtures("setup_guide")
@pytest.mark.usefixtures("setup_manage")
@pytest.mark.usefixtures("setup_ondemand")
class TestNavigation:

    @pytest.mark.sanity
    def test_4980944_Navigation_User_Experience(self):
        """
        https://jira.tivo.com/browse/CA-4091
        [TVE Web Portal2] - Navigation through all tabs for User experience
        https://testrail.tivo.com/index.php?/cases/view/4980944
        """

        self.log.step("Step 1: Login into the TiVo Online Portal")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.wtw_assertions.mainPageTabs_assert()
        self.log.step("Step 2: Navigating through What To watch submenus")
        self.wtw_assertions.whatToWatchSubMenus()
        self.log.step("Step 3: Verifying View All displays complete strip content")
        self.wtw_assertions.verify_ViewAllOfaStrip()
        self.log.step("Step 4: Navigating to ON Demand Page")
        self.ondemand_assertions.verify_OnDemand_submenus()
        self.log.step("Step 5: Navigating to Guide Page")
        self.guide_assertions.verifyGuidePage()
        self.log.step("Step 6: Navigating to My Shows Page")
        self.my_shows_assertions.verify_myShowsPage()
        self.log.step("Step 7: Navigating through Manage submenus")
        self.manage_assertions.managePageSubMenus()
        self.log.step("Step 8: Logo Click")
        self.manage_assertions.verify_logoClick()

    @pytest.mark.sanity
    @pytest.mark.skipif("cableco" in Settings.mso.lower(), reason="No Guest Experience for Cableco")
    def test_9916801_Navigation_Guest_User_Experience(self):
        """
        https://jira.tivo.com/browse/CA-4090
        Navigation through all tabs for Guest experience
        https://testrail.tivo.com/index.php?/cases/view/9916801
        """

        self.log.step("Step 1: Navigating to guide and verifying zipcode line up is displayed")
        self.guide_assertions.guide_page()
        self.log.step("Step 2: verifying the Sign In to Get This Show button is displayed")
        self.guide_assertions.assert_poster_present()
        """
            summary :This TC will navigate to my shows folder and verify the content
        """
        self.log.step("Step 3: Navigate to My Shows and verify the content")
        self.my_shows_page.go_to_MyShows()
        self.my_shows_assertions.my_show_message_assert()
        """
            summary :This TC will navigate to manage folder and also sub menu, Sign In button is displayed with
            a specific message
        """
        self.log.step("Step 4: Navigate to manage and submenus, verify the content")
        self.manage_page.go_to_Manage()
        self.manage_assertions.manage_to_do_list()
        self.manage_assertions.manage_onepass_manager()
        self.manage_assertions.manage_onepass_quick_select()
        self.manage_assertions.manage_recording_activity()
        """
            summary :This TC will verify the guest user header content
        """
        self.log.step("Step 5: Verify the header content, logo,sign in,search bar,etc")
        self.wtw_assertions.guest_user_logo_assert()
        self.wtw_assertions.searchBar_assert()
        self.wtw_assertions.signInLink_assert()
        self.wtw_assertions.signOutLink_NotPresent_assert()
        self.wtw_assertions.box_selection_drop_down_assert()
        self.log.step("step 6: check the logo")
        self.manage_assertions.verify_logoClick()
        """
            summary :This TC will navigate to What to watch sub menu and verify the content of each menu
        """
        self.log.step("Step 7: Navigate to WTW submenu verify the content")
        self.wtw_assertions.verify_onTvTodayPage()
        self.wtw_assertions.verify_sportsPage()
        self.wtw_assertions.verify_moviesPage()
        self.wtw_assertions.verify_tvSeriesPage()
        self.wtw_assertions.verify_kidsPage()
        """
            summary :verify the view_all option, poster content and sign in page
        """
        self.log.step("Step 8: Click on the view all and select an asset")
        self.wtw_page.feature_content()
        self.wtw_assertions.view_all_display()
        self.log.step("Step 9: verifying the sign In to Get This Show button is displayed ")
        self.wtw_page.poster_content()
        self.log.step("Step 10: The user is redirected to Sign In page.")
        self.wtw_page.verify_PageLoginLoaded()

    @pytest.mark.bat
    def test_10190189_Navigation_Menu_Rule(self):
        """
        https://jira.tivo.com/browse/CA-4565
        Interactions - Global Navigation - Menus rule
        https://testrail.tivo.com/index.php?/cases/view/10190189
        """

        self.log.info("Step 1: Login in Web-portal")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.log.info("Step 1: Expectancy: What to Watch page is displayed")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Check Menu and Submenu when the WTW page is displayed")
        self.log.info("Step 2: Expectancy: The nav is expanded and the selected options are highlighted "
                      "(Menus and Submenus)")
        self.wtw_assertions.assert_WTW_highlighted()
        self.wtw_assertions.assert_JustForMe_highlighted()
        self.log.info("Step 3: Select the Manager menu and check Menu and Submenu..")
        self.manage_page.go_to_Manage()
        self.log.info("Step 3: Expectancy: The nav is expanded and the selected options are highlighted "
                      "(Menus and Submenus).")
        self.manage_assertions.assert_Manage_highlighted()
        self.manage_assertions.assert_ToDoList_highlighted()
        self.log.info("Step 4: Select the Guide menu.")
        self.guide_page.go_to_Guide()
        self.log.info("Step 4: Expectancy: The menu is successfully displayed and the Submenu is hidden."
                      " The selected option (Menu) is highlighted.")
        self.guide_assertions.assert_Guide_highlighted()
        self.guide_assertions.assert_Manage_submenu_hidden()
        self.log.info("Step 5: Select My shows menu.")
        self.my_shows_page.go_to_MyShows()
        self.log.info("Step 5: Expectancy: The menu is successfully displayed and the Submenu is hidden."
                      " The selected option (Menu) is highlighted.")
        self.my_shows_assertions.assert_MyShows_highlighted()
        self.my_shows_assertions.assert_Manage_submenu_hidden()
        self.log.info("Step 6: Select a TV Show/ Movie/Series/Person content page from WTW strips.")
        self.wtw_page.go_to_What_to_Watch()
        self.wtw_page.select_tile_from_strip(WhatToWatchLabels.LBL_WTW_STRIP_OnTVToday)
        self.wtw_page.select_an_asset()
        self.log.info("Step 6: Expectancy: The menu is successfully displayed and the Submenu bar is hidden."
                      " The menu is unselected and the nav bar is collapsed")
        self.wtw_assertions.assert_Menu_displayed()
        self.wtw_assertions.assert_WTW_not_highlighted()
        self.wtw_assertions.assert_WTW_submenu_hidden()
