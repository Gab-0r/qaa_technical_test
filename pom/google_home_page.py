from utilities.browser_interactions import BrowserInteractions
from pom.locators.google_home_locators import GoogleHomeLocators as locators


class GoogleHomePage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def to_home(self, url: str):
        self.browser_interactions.open_page(url)

    def fill_search_field(self, text: str):
        return self.browser_interactions.input_text(locators.SEARCH_BAR, text)

    def click_search(self):
        self.browser_interactions.click_element(locators.SEARCH_BUTTON)

    def search_for(self, text2search: str):
        if self.fill_search_field(text2search):
            self.click_search()
            return True

        else:
            return False



