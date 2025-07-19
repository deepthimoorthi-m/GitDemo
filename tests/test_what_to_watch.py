from webportal.client_api.what_to_watch.conftest import *
from webportal.client_api.manage.conftest import *
from webportal.client_api.guide.conftest import *
from webportal.client_api.my_shows.conftest import *


@pytest.mark.usefixtures("setup_what_to_watch")
@pytest.mark.usefixtures("setup_manage")
@pytest.mark.usefixtures("setup_guide")
class TestWhatToWatch:

    @pytest.mark.sanity
    def test_4980955_signInSignOut(self):
        """ https://testrail.tivo.com/index.php?/cases/view/4980955 """
        self.log.step("Step 1: Click on SignIn button")
        self.wtw_page.select_button_sign_in()
        self.log.step("Step 1: Login (enter credentials)")
        self.wtw_page.log_in()
        self.log.step("Step 1: Expectancy: Verify if Login is successful and What to Watch page is successfully displaying")
        self.wtw_assertions.mainPageTabs_assert()
        self.log.step("Step 2: Click on 'Sign Out' button")
        self.wtw_page.log_out()
        self.log.step("Step 2: Expectancy 1: Verify 'SignIn link' is displayed")
        self.wtw_assertions.signInLink_assert()
        self.log.step("Step 2: Expectancy 2: Verify that 'Box' selection dropdown is NOT displayed")
        self.wtw_assertions.mainDropDownMenu_NotPresent_assert()
        self.log.step("Step 2: Expectancy 3: Verify 'SignOut' link is NOT displayed")
        self.wtw_assertions.signOutLink_NotPresent_assert()

    @pytest.mark.sanity
    def test_4980949_createOnePass(self, setup_myshows_delete_everything, setup_login):
        """
        https://jira.tivo.com/browse/CA-4195
        Create OnePass
        https://testrail.tivo.com/index.php?/cases/view/4980949
        """
        self.guide_page.go_to_Guide()  # this step is needed for refresh after deleting the OnePass
        self.log.step("Step 1: Navigate to the first show from first strip")
        self.wtw_page.go_to_What_to_Watch()
        self.wtw_page.select_tile_from_strip()
        # self.wtw_assertions.assert_Remove_Modify_OnePass()  # extra verification, makes sure there is no Onepass created
        self.wtw_page.select_Get_this_Show()
        self.log.step("Step 1: Expectancy: Assert this Show dialog is displayed")
        self.wtw_assertions.assert_Get_this_Show_displayed()
        self.log.step("Step 2: Select Create OnePass option")
        self.wtw_page.select_create_OnePass_option()
        self.log.step("Step 2: Expectancy: Verify OnePass dialog displayed")
        self.wtw_assertions.assert_OnePass_Options_displayed()
        self.log.step("Step 3: Press Create OnePass button")
        self.wtw_page.select_create_OnePass_button()
        self.log.step("Step 3.A: Expectancy:  Verify Create OnePass whisper notification is displayed")
        self.wtw_assertions.assert_Create_Whisper_OnePass()
        self.log.step("Step 3.B: Expectancy: Verify Modify option is displayed in asset detail page")
        self.wtw_assertions.assert_Modify_OnePass()
        self.log.info(" Memorize Show name, Season, Episode name for the newly created OnePass")
        showName, season, episodeName = self.wtw_page.asset_with_OnePass()
        self.log.info(f'\nThe asset (ShowName, Season, EpisodeName) with OnePass is: {showName, season, episodeName}\n')
        self.log.step("Step 4: Nagivate to OnePass Manage")
        self.manage_page.go_to_Manage()
        self.manage_page.select_OnePass_Manager()
        # when all subscriptions will be deleted at start,
        # there will be no need to scroll to end; may fail due to lazy loading (not applicable in our automation
        # test environment, which will be ready soon)
        self.manage_page.scroll_till_page_end()
        self.log.step("Step 4: Expectancy: Assert the OnePass created at step 3 is displayed here")
        self.manage_assertions.assert_Asset_with_OnePass(showName)

    @pytest.mark.sanity
    def test_12777499_cancelOnePass(self, setup_myshows_delete_everything, setup_what_to_watch_create_OnePass):
        """
        https://jira.tivo.com/browse/CA-4197
        Cancel OnePass
        https://testrail.tivo.com/index.php?/cases/view/12777499
        """
        self.log.step("Step 1: Go to asset detail page and click Modify option")
        self.wtw_assertions.assert_Modify_OnePass()  # extra verification
        self.wtw_page.select_Modify()
        self.log.step("Step 1: Expectancy: Verify Modify OnePass dialog is displayed")
        self.wtw_assertions.assert_Modify_displayed()
        self.log.step("Step 2: Select Cancel OnePass option")
        self.wtw_page.select_Cancel()
        self.log.step("Step 2: Expectancy: Verify Cancel OnePass dialog is displayed")
        self.wtw_assertions.assert_Cancel_displayed()
        self.log.step("Step 3: Press Cancel button")
        self.wtw_page.confirm_Cancel()
        self.log.step("Step 3.A: Expectancy: Verify Cancel OnePass whisper notification is displayed")
        self.wtw_assertions.assert_Cancel_Whisper_OnePass()
        self.log.step("Step 3.B: Expectancy: Verify Modify option is not displayed")
        self.wtw_assertions.assert_Remove_Modify_OnePass()

    @pytest.mark.bat
    def test_12793770_navigationShareOption(self):
        """
        https://jira.tivo.com/browse/CA-4567
        Interactions - Global Navigation - Share
        https://testrail.tivo.com/index.php?/cases/view/12793770
        """
        self.log.info("Step 1: Enter Webportal URL and log in to the application")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Select any show to open an Info card")
        self.wtw_page.select_tile_from_strip(WhatToWatchLabels.LBL_WTW_STRIP_OnTVToday)
        self.log.info("Step 2: Expectancy: Show Info card is displayed")
        self.wtw_assertions.assert_Info_card_displayed()
        self.log.info("Step 3: Click the share icon")
        self.wtw_page.select_share()
        self.log.info("Step 3: Expectancy: Verify the pop up contains:"
                      " A. Title: <Share this show>"
                      " B. Facebook"
                      " C. Twitter"
                      " D. Email")
        self.wtw_assertions.assert_ShareFormat()

    @pytest.mark.bat
    def test_10190203_navigationShareFacebook(self):
        """
        https://jira.tivo.com/browse/CA-4567
        Interactions - Global Navigation - Facebook Share
        https://testrail.tivo.com/index.php?/cases/view/10190203
        """
        self.log.info("Step 1: Enter Webportal URL and log in to the application")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Select any show to open an Info card")
        self.wtw_page.select_tile_from_strip(WhatToWatchLabels.LBL_WTW_STRIP_OnTVToday)
        self.log.info("Step 2: Expectancy: Show Info card is displayed")
        self.wtw_assertions.assert_Info_card_displayed()
        self.log.info("Step 3: Click the share icon")
        self.wtw_page.select_share()
        self.log.info("Step 3: Expectancy A: Share pop up is displayed")
        self.wtw_assertions.assert_Share_displayed()
        # This is an additional verification needed in automation, as verifying in Facebook is change prone.
        self.log.info("Step 3: Expectancy B: Share URL is correct")
        self.wtw_assertions.assert_Facebook_share_format()
        self.log.info("Step 4: Click Facebook icon")
        self.wtw_page.select_Facebook()
        self.log.info("Step 4: Expectancy: "
                      "A. The Facebook share sheet is opened as a popup overlay"
                      "B. User can choose to create a caption or post without creating additional text"
                      "C. The share sheet contains a poster and a link to the TiVo Portal Home page"
                      "D. On posting, only a subset of metadata is displayed in Facebook:")
        self.wtw_assertions.assert_Facebook_displayed()

    @pytest.mark.bat
    def test_12793767_navigationShareTwitter(self):
        """
        https://jira.tivo.com/browse/CA-4567
        Interactions - Global Navigation - Twitter Share
        https://testrail.tivo.com/index.php?/cases/view/12793767
        """
        self.log.info("Step 1: Enter Webportal URL and log in to the application")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Select any show to open an Info card")
        self.wtw_page.select_tile_from_strip(WhatToWatchLabels.LBL_WTW_STRIP_OnTVToday)
        self.log.info("Step 2: Expectancy: Show Info card is displayed")
        self.wtw_assertions.assert_Info_card_displayed()
        self.log.info("Step 3: Click the share icon")
        self.wtw_page.select_share()
        self.log.info("Step 3: Expectancy A: Share pop up is displayed")
        self.wtw_assertions.assert_Share_displayed()
        # This is an additional verification needed in automation, as verifying in Twitter is change prone.
        self.log.info("Step 3: Expectancy B: Share URL is correct")
        self.wtw_assertions.assert_Twitter_share_format()
        self.log.info("Step 4: Click Twitter icon")
        self.wtw_page.select_Twitter()
        self.log.info("Step 4: Expectancy: "
                      "A. The Twitter share sheet is opened as a popup overlay")
        self.wtw_assertions.assert_Twitter_displayed()

    @pytest.mark.bat
    def test_12793769_navigationShareEmail(self):
        """
        https://jira.tivo.com/browse/CA-4567
        Interactions - Global Navigation - Email Share
        https://testrail.tivo.com/index.php?/cases/view/12793769
        """
        self.log.info("Step 1: Enter Webportal URL and log in to the application")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Select any show to open an Info card")
        self.wtw_page.select_tile_from_strip(WhatToWatchLabels.LBL_WTW_STRIP_OnTVToday)
        self.log.info("Step 2: Expectancy: Show Info card is displayed")
        self.wtw_assertions.assert_Info_card_displayed()
        self.log.info("Step 3: Click the share icon")
        self.wtw_page.select_share()
        self.log.info("Step 3: Expectancy A: Share pop up is displayed")
        self.wtw_assertions.assert_Share_displayed()
        # This is an additional verification needed in automation, as verifying in Email is not possible (not browser).
        self.log.info("Step 3: Expectancy B: Share URL is correct")
        self.wtw_assertions.assert_Email_share_format()
        # Cannot verify step 4: Email pop up is displayed, as email is displayed in an application window (not browser)
