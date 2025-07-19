from webportal.client_api.search.labels import SearchLabels
from webportal.client_api.search.conftest import *
from webportal.client_api.what_to_watch.conftest import *


@pytest.mark.usefixtures("setup_what_to_watch")
@pytest.mark.usefixtures("setup_search")
class TestSearch:

    @pytest.mark.sanity
    def test_4980953_verify_movie_from_search_field(self, setup_get_movie):
        """
        https://testrail.tivo.com/index.php?/cases/view/4980953
        https://jira.tivo.com/browse/CA-4095
        summary :This TC will search for a movie from search field and verify the item entered from search field
        is displayed or not.
        """
        self.log.info("Pre-Requisite : Login to web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.step("Step 1 : Click the Search option from the global navigation")
        self.search_page.text_search_field(self.movie)
        self.log.step("Step 1. Expectancy : Verify the entered Item in the Displayed List")
        self.search_assertions.verify_search_list_results(self.movie)
        self.log.step("Step 2 : Close the search field")
        self.search_page.close_search_field()
        self.log.step("Step 2. Expectancy A : Assert if the element not present")
        self.search_assertions.search_menu_assert()
        self.log.step("Step 2. Expectancy B : Assert if the element is present in the page ")
        self.search_assertions.search_field_not_present_assert()

    @pytest.mark.bat
    def test_12783900_verify_non_episodic_from_search_field(self, setup_get_nonepisodic):
        """
        https://testrail.tivo.com/index.php?/cases/view/12783900
        https://jira.tivo.com/browse/CA-4543
        summary :This TC will search for a Non-Episodic show from search field and verify the item entered from search
        field is displayed or not.
        """
        self.log.info("Pre-Requisite: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1 : Click the Search option from the global navigation")
        self.search_page.text_search_field(self.nonepisodic)
        self.log.info("Step 1. Expectancy : Verify the entered Item in the Displayed List")
        self.search_assertions.verify_search_list_results(self.nonepisodic)
        self.log.info("Step 2 : Close the search field")
        self.search_page.close_search_field()
        self.log.info("Step 2. Expectancy A : Assert if the element not present")
        self.search_assertions.search_menu_assert()
        self.log.info("Step 2. Expectancy B : Assert if the element is present in the page ")
        self.search_assertions.search_field_not_present_assert()

    @pytest.mark.bat
    def test_12783899_verify_episodic_show_from_search_field(self, setup_get_episodic):
        """
        https://testrail.tivo.com/index.php?/cases/view/12783899
        https://jira.tivo.com/browse/CA-4542
        summary :This TC will search for a Episodic show from search field and verify the item entered from search
        field is displayed or not.
        """
        self.log.info("Pre-Requisite : Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1 : Click the Search option from the global navigation")
        self.search_page.text_search_field(self.episodic)
        self.log.info("Step 1. Expectancy : Verify the entered Item in the Displayed List")
        self.search_assertions.verify_search_list_results(self.episodic)
        self.log.info("Step 2 : Close the search field")
        self.search_page.close_search_field()
        self.log.info("Step 2. Expectancy A : Assert if the element not present")
        self.search_assertions.search_menu_assert()
        self.log.info("Step 2. Expectancy B : Assert if the element is present in the page ")
        self.search_assertions.search_field_not_present_assert()

    @pytest.mark.bat
    def test_12783898_verify_Person_from_search_field(self, setup_get_person):
        """
        https://testrail.tivo.com/index.php?/cases/view/12783898
        https://jira.tivo.com/browse/CA-4540
        summary :This TC will search for a actor/filmmakers from search field and verify the item entered from search
        field is displayed or not.
        """
        self.log.info("Pre-Requisite : Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1 : Click the Search option from the global navigation")
        self.search_page.text_search_field(self.person)
        self.log.info("Step 1. Expectancy : Verify the entered Item in the Displayed List")
        self.search_assertions.verify_search_results_person(self.person)
        self.log.info("Step 2 : Close the search field")
        self.search_page.close_search_field()
        self.log.info("Step 2. Expectancy A : Assert if the element not present")
        self.search_assertions.search_menu_assert()
        self.log.info("Step 2. Expectancy B : Assert if the element is present in the page ")
        self.search_assertions.search_field_not_present_assert()

    @pytest.mark.bat
    def test_10190190_SearchResultFormatEpisodic(self, setup_get_episodic):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Episodic
        https://testrail.tivo.com/index.php?/cases/view/10190190
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Click Search icon, "
                      "enter a valid Episode name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(self.episodic)
        self.search_page.open_in_search(self.episodic)
        episode_title = self.search_page.find_episode_title()
        self.search_page.text_search_field(episode_title)
        self.log.info("Step 2: Expectancy: The system should list following details for a "
                      "TV Show suggestion in the drop-down: "
                      "Left Side: "
                      "- Poster"
                      "Right Side"
                      " Episodic:"
                      "- Title: <series name> <Episode name>"
                      "- Body 1: <premiere year> -<<finale year>/Current>"
                      "- Body 2: <genres>")
        type_title = "episode"
        self.search_assertions.verify_search_item_format(title=episode_title, type_title=type_title)

    @pytest.mark.bat
    def test_12788236_SearchResultFormatMovie(self, setup_get_movie):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Movie
        https://testrail.tivo.com/index.php?/cases/view/12788236
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.step("Step 1: Click Search icon, "
                      "enter a valid Movie name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(self.movie)
        self.log.step("Step 1: Expectancy: The system should list following details for a "
                      "Movie:"
                      "- For <movie title>, see <movie title> in Program Data."
                      "- Truncate if necessary using Middle Truncation and preserve the year."
                      "- Enclose (<year>) in parenthesis.")
        type_title = "movie"
        self.search_assertions.verify_search_item_format(title=self.movie, year=self.movie_year, type_title=type_title)
        self.log.step("Step 2 : Close the search field")
        self.search_page.close_search_field()
        self.log.step("Step 2. Expectancy A : Assert if the element not present")
        self.search_assertions.search_menu_assert()
        self.log.step("Step 2. Expectancy B : Assert if the element is present in the page ")
        self.search_assertions.search_field_not_present_assert()

    @pytest.mark.bat
    def test_12788235_SearchResultFormatPerson(self, setup_get_person):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Person
        https://testrail.tivo.com/index.php?/cases/view/12788235
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Click Search icon, "
                      "enter a valid Person name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(self.person)
        self.log.info("Step 2: Expectancy: The system should list following details for a "
                      "Person:"
                      "- Truncate <person name> if necessary using Full Word Truncation."
                      "- Icon trails person name."
                      "- For <generic person icon>, see Person poster art in Content Image Selection.")
        type_title = "person"
        self.search_assertions.verify_search_item_format(title=self.person, type_title=type_title)

    @pytest.mark.bat
    def test_12788237_SearchResultFormatSeries(self, setup_get_series):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Series
        https://testrail.tivo.com/index.php?/cases/view/12788237
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Click Search icon, "
                      "enter a valid Series name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(self.series)
        self.log.info("Step 2: Expectancy: The system should list following details for a TV Show "
                      "suggestion in the drop-down:"
                      "Left Side:"
                      "- Poster"
                      "Series:"
                      "- See <series title> in Program Data. Truncate if necessary using Partial Word Truncation."
                      "- Body 1: <premiere year> "
                      "- Body 2: <rating>"
                      "- Body 3: <genres>)")
        type_title = "series"
        self.search_assertions.verify_search_item_format(title=self.series, type_title=type_title)

    @pytest.mark.bat
    def test_12788238_SearchResultFormatSportTeam(self):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Sport Team
        https://testrail.tivo.com/index.php?/cases/view/12788238
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Click Search icon, "
                      "enter a valid Sport Team name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(SearchLabels.LBL_SEARCH_SPORT_TEAM)
        self.log.info("Step 2: Expectancy: The system should list following details for a TV Show"
                      "Left Side:"
                      "- Poster"
                      "Series:"
                      "- Team:"
                      "- Truncate <team name> if necessary using Full Word Truncation.")
        type_title = "sport_team"
        self.search_assertions.verify_search_item_format(title=SearchLabels.LBL_SEARCH_SPORT_TEAM, type_title=type_title)

    @pytest.mark.bat
    def test_12788239_SearchResultFormatNonEpisodic(self, setup_get_nonepisodic):
        """
        https://jira.tivo.com/browse/CA-4566
        Interactions - Global Navigation - Search results format Non Episodic
        https://testrail.tivo.com/index.php?/cases/view/12788239
        """
        self.log.info("Step 1: Login to Web-portal")
        self.search_page.select_button_sign_in()
        self.search_page.log_in()
        self.log.info("Step 1: Expectancy: The What to Watch page is displayed.")
        self.wtw_assertions.assert_OnTVToday()
        self.log.info("Step 2: Click Search icon, "
                      "enter a valid Non Episodic name as search criteria in the search text box."
                      "Check drop-down is displayed.")
        self.search_page.text_search_field(self.nonepisodic)
        self.log.info("Step 2: Expectancy: The system should list following details for a TV Show:"
                      "Left Side:"
                      "- Poster"
                      "Non-episodic:"
                      "- For <non-episodic title>, see <non-episodic title> in Program Data. "
                      "Truncate if necessary using Partial Word Truncation.")
        type_title = "non_episodic"
        self.search_assertions.verify_search_item_format(title=self.nonepisodic, type_title=type_title)
