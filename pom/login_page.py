import os

from utilities.browser_interactions import BrowserInteractions
from pom.locators.login_page_locators import LoginPageLocators as locators
from utilities.constants import Constants
from dotenv import load_dotenv

load_dotenv()


class LoginPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions
        self.cons = Constants

    # Returns the entire expected message from its name
    def _get_message(self, msg_name: str):
        msgs = {
            "correct login": self.cons.login_message,
            "incorrect username": self.cons.incorrect_username,
            "incorrect password": self.cons.incorrect_password
        }
        return msgs[msg_name]

    # Enters user and password, both correct and from .env file
    def enter_user_pass(self, username: str, password: str):
        if self.browser_interactions.input_text(locators.USERNAME_FIELD, username):
            if self.browser_interactions.input_text(locators.PASSWORD_FIELD, password):
                return True
        return False

    # Redirects to the login page
    def to_login_page(self, url: str):
        self.browser_interactions.open_page(url)

    # Clicks on login button
    def click_login(self):
        self.browser_interactions.click_element(locators.LOGIN_BUTTON)

    # Check if the messages are the expected
    def check_login_message (self, msg_name: str):
        login_message = self.browser_interactions.get_element(locators.LOGIN_MESSAGE).text
        return login_message.__contains__(self._get_message(msg_name))

    # Check if login is correct. Check if the logout button appears
    def check_login(self):
        return self.browser_interactions.element_is_visible(locators.LOGOUT_BUTTON)

    # Enters a username in the username field. It can be the correct one (from .env) or an invalid one
    # defined in a test case
    def enter_username(self, which="correct", username=" "):
        if which == "correct":
            self.browser_interactions.input_text(locators.USERNAME_FIELD, os.getenv("USERNAME"))
        elif which == "invalid":
            self.browser_interactions.input_text(locators.USERNAME_FIELD, username)

    # Enters a password in the password field. It can be the correct one (from .env) or an invalid one
    # defined in a test case
    def enter_password(self, which="correct", password=" "):
        if which == "correct":
            self.browser_interactions.input_text(locators.PASSWORD_FIELD, os.getenv("PASSWORD"))
        elif which == "invalid":
            self.browser_interactions.input_text(locators.PASSWORD_FIELD, password)
