from behave import step
from pom.results_page import ResultsPage


@step("The user goes to the search results page,and the first {n} results contain the word {word}")
def check_results(context, n: str, word: str):
    context.results_page = ResultsPage(context.browser_interactions)
    assert context.results_page.check_results(n, word), f"at least one result does not contains the word {word}"
