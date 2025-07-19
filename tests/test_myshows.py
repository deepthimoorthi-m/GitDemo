from webportal.client_api.what_to_watch.conftest import *
from webportal.client_api.guide.conftest import *
from webportal.client_api.my_shows.conftest import *


@pytest.mark.usefixtures("setup_my_shows")
@pytest.mark.usefixtures("setup_what_to_watch")
@pytest.mark.usefixtures("setup_guide")
class TestMyShows:

    @pytest.mark.sanity
    def test_4980952_CreateDeleteBookmark(self, setup_myshows_delete_everything):
        """ https://testrail.tivo.com/index.php?/cases/view/4980952 """
        self.log.step("Login to current account")
        self.wtw_page.select_button_sign_in()
        self.wtw_page.log_in()
        self.wtw_assertions.mainPageTabs_assert()
        self.log.step("Go To 'What To Watch - Movies' and select a movie")
        self.my_shows_page.go_to_Movies()
        movie = self.my_shows_page.search_movie_and_select()
        self.log.step("Create Bookmark")
        self.my_shows_page.create_bookmark()
        self.log.step("Go to MyShows")
        self.my_shows_assertions.assert_shortcut_delete_show()
        self.my_shows_page.go_to_MyShows()
        self.log.step("Delete Movie")
        self.my_shows_page.delete_movie(movie)
        self.log.step("Verify movie is deleted from MyShows")
        self.my_shows_assertions.assert_streaming_movies_folder_present()
