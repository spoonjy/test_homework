from Panda_Plugins.Pages.base_page import BasePage
from Panda_Plugins.Locators.shiningpanda_loc import PandaPageLoc

link = "https://plugins.jenkins.io/shiningpanda/"


class MainPage(BasePage):
    def verify_panda_text(self):
        panda_title_text = self.chrome.find_element(*PandaPageLoc.shinning_panda_title_loc).text
        assert panda_title_text == 'ShiningPanda', 'Title is not ShiningPanda'

