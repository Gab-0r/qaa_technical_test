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
    assert_login(context.login_page.check_login())


@step("The {msg} message displayed is the expected")
def check_msg(context, msg: str):
    context.login_page = LoginPage(context.browser_interactions)
    assert_message(context.login_page.check_login_message(msg), msg)


@step("The user enters a {which} username {username}")
def input_username(context, which: str, username: str):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.enter_username(which=which, username=username)


@step("Enters a correct username")
def input_ok_username(context):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.enter_username()


@step("Enters a correct password")
def input_ok_password(context):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.enter_password()


@step("The user enters an {which} password {password}")
def input_password(context, which: str, password: str):
    context.login_page = LoginPage(context.browser_interactions)
    context.login_page.enter_password(which=which, password=password)
