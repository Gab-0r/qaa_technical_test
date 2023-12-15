import time

from behave import step
from pom.google_home_page import GoogleHomePage


@step("The user is on the Google homepage")
def open_home_page(context):
    context.home_page = GoogleHomePage(context.browser_interactions)
    context.home_page.to_home("https://www.google.com")


@step("The user type {text2search} into the search field and clicks on the Google search button")
def make_google_search(context, text2search: str):
    context.home_page = GoogleHomePage(context.browser_interactions)
    context.home_page.search_for(text2search)
