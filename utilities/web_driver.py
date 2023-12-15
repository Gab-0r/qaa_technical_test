from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

class WebDriverManager:
    def __init__(self, driver_mode: str):
        self.driver_mode = driver_mode

    def create_chrome_driver(self) -> Chrome:
        if self.driver_mode == "headless":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = Chrome(options=options)
            return driver

        elif self.driver_mode == "normal":
            return Chrome()
