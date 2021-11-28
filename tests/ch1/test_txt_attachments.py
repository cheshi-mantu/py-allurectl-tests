import json
import os

import allure
from allure import attachment_type


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach")
def test_attach_small_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "chekhov.txt"), name="normal 10 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending normal text attach")
def test_attach_normal_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "blake.txt"), name="normal 200 kbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending medium text attach")
def test_attach_medium_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "ktulhu.txt"), name="normal 3 Mbytes txt attach", attachment_type=attachment_type.TEXT)

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending big text attach")
def test_attach_big_text():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "icona.txt"), name="normal 10 Mbytes txt attach", attachment_type=attachment_type.TEXT)