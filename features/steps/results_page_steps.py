import time

from behave import step
from pom.results_page import ResultsPage
from utilities.asserts_helper import *

@step("The user goes to the search results page,and the first {n} results contain the word {word}")
def check_results(context, n: str, word: str):
    context.results_page = ResultsPage(context.browser_interactions)
    assert_words_in_result(context.results_page.check_results(n, word), word)


@step("The user clicks on the first result link")
def click_first_result(context):
    context.results_page = ResultsPage(context.browser_interactions)
    context.results_page.to_first_result()
