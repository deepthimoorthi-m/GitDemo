from webportal.client_api.my_shows.conftest import *
from webportal.client_api.manage.conftest import *
from webportal.client_api.guide.conftest import *


@pytest.mark.usefixtures("setup_guide")
@pytest.mark.usefixtures("setup_my_shows")
@pytest.mark.usefixtures("setup_manage")
class TestGuide:

    @pytest.mark.sanity
    def test_4980947_WatchLiveTvFromGuide(self):
        """https://jira.tivo.com/browse/CA-4147
        [TVE Web Portal2] Guide - Watch Live TV
        Summary : To watch a Live tv show from guide
        """
        self.log.info("Pre-Requisite: Login to Web-portal")
        self.guide_page.select_button_sign_in()
        self.guide_page.log_in()
        self.log.step("Step 1 : Navigate to Guide and select a show that it is currently airing now.")
        self.guide_page.go_to_Guide()
        self.guide_page.Nav_to_an_airing_show_from_Guide()
        self.log.step("Step 1. Expectancy : Verifying the Live TV button displayed or not ")
        self.guide_assertions.assert_LiveTv_Button()
        self.log.step("Step 2 : Click on Live TV button")
        self.guide_page.Select_Live_Tv_Button()
        self.log.step("Step 2.Expectancy : Embedded player is displayed and show is successfully playing.")
        self.guide_assertions.assert_LiveTv_Screen()

    @pytest.mark.sanity
    @pytest.mark.skipif("cableco" in Settings.mso.lower(), reason="No record can be played")
    def test_4980954_Record_And_Play_From_MyShows(self, setup_myshows_delete_everything, setup_recordable_channels):
        """https://jira.tivo.com/browse/CA-4093
        [TVE Web Portal2] - Guide - Create a record and play it from My Shows
        Summary : this TC is to record the current airing shows from guide and play that from my shows
        Run only for Retail mso and CableCo mso with nDVR for recordable channels
        """
        self.log.info("Pre-Requisite: Login to Web-portal")
        self.guide_page.select_button_sign_in()
        self.guide_page.log_in()
        self.log.step("Step 1 : Go to Guide and schedule the Record")
        self.guide_page.go_to_Guide()
        self.guide_page.Get_this_Show_From_Guide()
        (recorded_asset, recorded_asset_1) = self.guide_page.Schedule_Record_from_Guide(self.recordable_channel)
        self.log.step("Step 1. Expectancy : Verify the record schedule")
        self.guide_assertions.assert_verify_recorded_element()
        self.log.step("Step 2 : Go to My-Shows and play the recorded asset")
        self.guide_page.Nav_My_Show_and_select_asset(recorded_asset, recorded_asset_1)
        self.log.step("Step 2. Expectancy : Verify the player screen")
        self.guide_assertions.assert_my_recording_Screen()

    @pytest.mark.bat
    def test_4980923_Close_player_and_check_the_recording_status(self, setup_myshows_delete_everything,
                                                                 setup_todolist_delete_all, setup_recordable_channels):
        """https://jira.tivo.com/browse/CA-4561
        [TVE Web Portal2] - Guide - Create a record, play it from My Shows and close the player screen and check for the
        recording status.
        Summary : this TC is to record the current airing shows from guide, play it from my shows and close the player
        check for recording status.
        Run only for Retail mso and CableCo mso with nDVR for recordable channels
        """
        self.log.info("Step 1 : Go to Guide and schedule the Record")
        self.guide_page.go_to_Guide()
        self.guide_page.Get_this_Show_From_Guide()
        (recorded_asset, recorded_asset_1) = self.guide_page.Schedule_Record_from_Guide(self.recordable_channel)
        self.log.info("Step 1. Expectancy : Verify the record schedule")
        self.guide_assertions.assert_verify_recorded_element()
        self.log.info("Step 2 : Go to My-Shows, play the recorded asset and close the player screen")
        self.guide_page.Nav_My_Show_and_select_asset(recorded_asset, recorded_asset_1)
        # self.guide_page.close_player_screen()
        self.log.info("Step 2. Expectancy : Verify the player screen is closed and status of the recording icon")
        self.guide_assertions.assert_LiveTv_Screen_Not_Present()
        self.guide_assertions.assert_Recording_icon_present()
