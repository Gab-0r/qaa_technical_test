from utilities.browser_interactions import BrowserInteractions
from pom.locators.results_page_locators import ResultsPageLocators as locators


class ResultsPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    def check_results(self, results_to_check: str, word_to_search: str):
        n = int(results_to_check) + 1
        results_text = [result.text.lower() for result in self.browser_interactions.get_elements(locators.RESULTS_TITLES)]
        bool_list = [result.__contains__(word_to_search.lower()) for result in results_text]
        bool_list = bool_list[:n]
        if any(bool_list):
            return True
        else:
            return False
