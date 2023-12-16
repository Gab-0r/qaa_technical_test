import os
import time

from behave import step
from pom.upload_file_page import UploadFilePage
from dotenv import load_dotenv
from utilities.asserts_helper import *

load_dotenv()


@step("The user is on the upload file page")
def to_upload_file_page(context):
    context.upload_file_page = UploadFilePage(context.browser_interactions)
    context.upload_file_page.to_upload_page(os.getenv("UPLOAD_FILE_PAGE"))


@step("The user attach a file")
def attach_file(context):
    context.upload_file_page = UploadFilePage(context.browser_interactions)
    assert_attach_file(context.upload_file_page.attach_file(os.getcwd() + os.getenv("FILE_TO_ATTACH")))


@step("Clicks on upload button")
def upload_file(context):
    context.upload_file_page = UploadFilePage(context.browser_interactions)
    context.upload_file_page.upload_file()


@step("The file is uploaded successfully")
def check_upload_msg(context):
    context.upload_file_page = UploadFilePage(context.browser_interactions)
    assert_uploaded_file(context.upload_file_page.check_upload())

