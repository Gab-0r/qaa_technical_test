import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_locator(raw_locator: tuple) -> tuple:
    strategy, selector = raw_locator
    strategies = {"ID": By.ID, "XPATH": By.XPATH, "CSS": By.CSS_SELECTOR}
    return strategies[strategy], selector


class BrowserInteractions:
    def __init__(self, driver: Chrome, time_out):
        self._driver = driver
        self.time_out = time_out

    def open_page(self, url: str):
        self._driver.get(url)

    def click_element(self, raw_locator: tuple):
        element = WebDriverWait(self._driver, self.time_out).until(
            EC.element_to_be_clickable(get_locator(raw_locator))
        )
        element.click()
