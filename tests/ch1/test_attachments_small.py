import json
import os

import allure
from allure import attachment_type

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment")
def test_attach_smallimage():

    current_folder = os.getcwd()
    print("Current folder:", current_folder)

    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach")
def test_attach_smalltext():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)