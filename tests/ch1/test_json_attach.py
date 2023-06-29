import allure
from allure import attachment_type

import time
import os

@allure.suite("cloud instance")
@allure.feature("sending attachments")
@allure.story("sending JSON attachments")
@allure.title("Sending JSON attachments")
def test_json_attach():
    print("sending JSON attachment")
    time.sleep(5)
    with allure.step("Sending fillable PDF to report as JSON request"):
        print("sending JSON attachment")
        allure.attach.file(os.path.join("resources", "request_example.json"), name="request example", attachment_type=attachment_type.JSON)
