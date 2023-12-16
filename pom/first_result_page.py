from utilities.browser_interactions import BrowserInteractions
from pom.locators.first_result_page_locators import FirstResultPageLocators as locators


class FirstResultPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def title_contains(self, word: str):
        title = self.browser_interactions.get_element(locators.TITLE).text.lower()
        if title.__contains__(word.lower()):
            return True
        else:
            return False
