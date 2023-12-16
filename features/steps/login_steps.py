import time

from behave import step
from pom.login_page import LoginPage
from utilities.asserts_helper import *
import os
from dotenv import load_dotenv

load_dotenv()


@step("The user is on the login page")
def to_login(context):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.to_login_page(os.getenv("LOGIN_URL"))


@step("The user enters its username and password")
def enter_info(context):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.enter_user_pass(os.getenv("USERNAME"), os.getenv("PASSWORD"))


@step("Clicks on login button")
def click_login(context):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.click_login()


@step("The user has logged successfully")
def check_login(context):
    context.login_page = LoginPage(context.browser_interactions)
    assert context.login_page.check_login(), "user cannot be logged"


@step("The {msg} message displayed is the expected")
def check_msg(context, msg: str):
    context.login_page = LoginPage(context.browser_interactions)
    assert context.login_page.check_login_message(msg), f"{msg} message is not the expected"
