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

def test_change_project_permissions():
    pass