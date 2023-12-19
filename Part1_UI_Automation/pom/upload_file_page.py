from utilities.browser_interactions import BrowserInteractions
from pom.locators.upload_file_page_locators import UploadFilePageLocators as locators
from utilities.constants import Constants as cons


class UploadFilePage:
    def __init__(self, browser_interactions: BrowserInteractions):
        self.browser_interactions = browser_interactions

    # Redirects to upload file page
    def to_upload_page(self, url):
        self.browser_interactions.open_page(url)

    # Attach a file
    def attach_file(self, file_root: str):
        return self.browser_interactions.input_text(locators.FILE_FIELD, file_root)

    # Upload the file using upload button
    def upload_file(self):
        self.browser_interactions.click_element(locators.UPLOAD_BUTTON)

    # Check if the file was uploaded checking the message displayed after the process is done
    def check_upload(self):
        msg = self.browser_interactions.get_element(locators.UPLOADED_MSG).text
        return msg.__contains__(cons.FILE_UPLOADED)
