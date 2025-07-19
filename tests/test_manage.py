from webportal.client_api.what_to_watch.conftest import *
from webportal.client_api.guide.conftest import *
from webportal.client_api.manage.conftest import *
from webportal.client_api.my_shows.conftest import *


@pytest.mark.usefixtures("setup_manage")
@pytest.mark.usefixtures("setup_my_shows")
@pytest.mark.usefixtures("setup_guide")
@pytest.mark.usefixtures("setup_what_to_watch")
class TestManage:

    @pytest.mark.sanity
    def test_12777498_modifyOnepass(self, setup_cancel_all_recordings, setup_what_to_watch_delete_subscriptions,
                                    setup_what_to_watch_create_OnePass):
        """
        https://jira.tivo.com/browse/CA-4196
        Modify OnePass
        https://testrail.tivo.com/index.php?/cases/view/12777498
        """
        self.log.step("Step 1: Go to OnePass detail page in Manage page")
        self.manage_page.go_to_Manage()
        self.manage_page.select_OnePass_Manager()
        self.manage_page.select_OnePass()
        self.manage_assertions.assert_Modify_OnePass()  # extra verification
        self.manage_page.select_Modify()
        self.log.step("Step 1: Expectancy: Verify Modify OnePass dialog is displayed")
        self.manage_assertions.assert_Modify_displayed()
        self.log.step("Step 2: Change Keep Until field and click Modify")
        # testcase doesn't require next test step - test can fail if an already modified onepass will be reused
        # self.manage_assertions.assert_KeepUntil_value()
        self.manage_page.select_KeepUntil()
        self.manage_page.select_UntilIDelete()
        self.manage_assertions.assert_KeepUntil_value_selected()  # extra verification
        self.manage_page.select_modify_OnePass_button()
        self.log.step("Step 2: Expectancy: Verify Modify OnePass whisper notification is displayed")
        self.manage_assertions.assert_Modify_Whisper_OnePass()
        self.log.step("Step 3: Select the newly modified OnePass")
        self.manage_page.select_OnePass()
        self.manage_assertions.assert_Modify_OnePass()  # extra verification
        self.log.step("Step 3: Expectancy: Verify Keep Until value is Until I Delete")
        self.manage_page.scroll_till_page_end()
        self.manage_assertions.assert_value_selected_OnePass()

    @pytest.mark.bat
    def test_9919690_addContentToDoList(self, setup_todolist_delete_all):
        """
        https://jira.tivo.com/browse/CA-4547
        Add a new content to the To-Do-List
        https://testrail.tivo.com/index.php?/cases/view/9919690
        """

        self.log.info("Step 1: Schedule a recording from Guide")
        self.guide_page.nav_to_guide_select_a_show()
        (recorded_asset, episode_name, episode_number, big_episode_name, element_visible) = self.guide_page.\
            schedule_record_from_guide_and_get_the_element()
        show_name = recorded_asset + " " + episode_number + episode_name
        self.log.info("Recorded Show: " + show_name)
        self.log.info("Step 1: Expectancy : Verify the record is scheduled")
        self.guide_assertions.verify_recorded_whisper(element_visible)
        self.log.info("Step 2: Navigate to Manage->To-Do-List and search for the recorded asset")
        self.manage_page.go_to_Manage()
        self.log.info("Step 2: Expectancy : Verify recorded element is present in To-Do-List")
        self.manage_assertions.verify_to_do_list_recorded_element_present(recorded_asset, big_episode_name,
                                                                          episode_number, episode_name)
