from utilities.browser_interactions import BrowserInteractions
from pom.locators.login_page_locators import LoginPageLocators as locators
from utilities.constants import Constants


class LoginPage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions
        self.cons = Constants

    def _get_message(self, msg_name: str):
        msgs = {
            "correct login": self.cons.login_message,
            "incorrect username": self.cons.incorrect_username,
            "incorrect password": self.cons.incorrect_password
        }
        return msgs[msg_name]

    def enter_user_pass(self, username: str, password: str):
        if self.browser_interactions.input_text(locators.USERNAME_FIELD, username):
            if self.browser_interactions.input_text(locators.PASSWORD_FIELD, password):
                return True
        return False

    def to_login_page(self, url: str):
        self.browser_interactions.open_page(url)

    def click_login(self):
        self.browser_interactions.click_element(locators.LOGIN_BUTTON)

    def check_login_message (self, msg_name: str):
        login_message = self.browser_interactions.get_element(locators.LOGIN_MESSAGE).text
        return login_message.__contains__(self._get_message(msg_name))

    def check_login(self):
        return self.browser_interactions.element_is_visible(locators.LOGOUT_BUTTON)