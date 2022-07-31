import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Panda_Plugins.Pages.panda_main_page import PandaMainPage


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@allure.story('Open ShiningPanda Page')
def test_open_page_verify_title(open_browser):
    link = "https://plugins.jenkins.io/shiningpanda/"
    panda_plugin_page = PandaMainPage(browser, link)
    panda_plugin_page.open()
    panda_plugin_page.verify_panda_text_title()
