from utilities.browser_interactions import BrowserInteractions
from pom.locators.google_home_locators import GoogleHomeLocators as locators


class GoogleHomePage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    # Redirects to home page
    def to_home(self, url):
        self.browser_interactions.open_page(url)

    # Enters a text into the search field
    def fill_search_field(self, text: str):
        return self.browser_interactions.input_text(locators.SEARCH_BAR, text)

    # Clicks on search button
    def click_search(self):
        self.browser_interactions.click_element(locators.SEARCH_BUTTON)

    # Make the whole search process
    def search_for(self, text2search: str):
        if self.fill_search_field(text2search):
            self.click_search()
            return True

        else:
            return False
