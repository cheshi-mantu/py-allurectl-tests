import allure
from allure import attachment_type

import time
import os

@allure.suite("cloud instance")
@allure.feature("sending attachments")
@allure.story("sending pdf attachments")
@allure.title("Sending PDF attachments")
def test_pdf_attach():
    print("sending PDF attachment")
    time.sleep(5)
    with allure.step("Sending fillable PDF to report"):
        print("sending PDF attachment")
        time.sleep(5)
        allure.attach.file(os.path.join("resources", "fillable.pdf"), name="fillable pdf", attachment_type=attachment_type.PDF)
        time.sleep(5)
        print("== just sent it")
