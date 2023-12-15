import time

from behave import step
from pom.google_home_page import GoogleHomePage


@step("The user is on the Google homepage")
def open_home_page(context):
    context.home_page = GoogleHomePage(context.browser_interactions)
    context.home_page.to_home("https://www.google.com")
    time.sleep(5)

