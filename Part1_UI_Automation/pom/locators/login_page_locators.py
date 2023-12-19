class LoginPageLocators:
    USERNAME_FIELD = ("ID", "username")
    PASSWORD_FIELD = ("ID", "password")
    LOGIN_BUTTON = ("XPATH", "//*[@id='login']/button")
    LOGIN_MESSAGE = ("ID", "flash-messages")
    LOGOUT_BUTTON = ("XPATH", "//*[@id='content']/div/a")
