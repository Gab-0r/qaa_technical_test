from utilities.browser_interactions import BrowserInteractions
from utilities.web_driver import WebDriverManager


# Before every scenario the web driver is created
def before_scenario(context, scenario):
    web_driver = WebDriverManager("normal").create_chrome_driver()
    context.browser_interactions = BrowserInteractions(web_driver, 10)