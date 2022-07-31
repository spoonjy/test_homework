from Panda_Plugins.Pages.base_page import BasePage
from Panda_Plugins.Locators.shiningpanda_loc import PandaPageLoc

link = "https://plugins.jenkins.io/shiningpanda/"


class PandaMainPage(BasePage):
    def verify_panda_text_title(self):
        panda_text_title = self.chrome.find_element(*PandaPageLoc.shinning_panda_title_loc).text
        assert panda_text_title == 'ShiningPanda', 'Title is not ShiningPanda'

