import time

from behave import step
from pom.first_result_page import FirstResultPage


@step("The user goes to the page, and the page title contains the word {word}")
def check_title(context, word: str):
    context.first_result_page = FirstResultPage(context.browser_interactions)
    assert context.first_result_page.title_contains(word), f"title does not contains the word {word}"
    time.sleep(5)