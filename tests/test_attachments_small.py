import json
import os

import allure
from allure import attachment_type

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending small text attach")
def test_attach_smalltext():
    with allure.step("txt attach"):
        allure.attach.file(os.path.join("resources", "chekhov.txt"), name="letter to the neighbour", attachment_type=attachment_type.TEXT)



@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 000")
def test_attach_smallimage_000():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 001")
def test_attach_smallimage_001():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 002")
def test_attach_smallimage_002():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 003")
def test_attach_smallimage_003():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 004")
def test_attach_smallimage_004():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 005")
def test_attach_smallimage_005():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 006")
def test_attach_smallimage_006():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 007")
def test_attach_smallimage_007():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 008")
def test_attach_smallimage_008():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 009")
def test_attach_smallimage_009():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 010")
def test_attach_smallimage_010():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 011")
def test_attach_smallimage_011():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 012")
def test_attach_smallimage_012():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 013")
def test_attach_smallimage_013():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 014")
def test_attach_smallimage_014():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 015")
def test_attach_smallimage_015():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 016")
def test_attach_smallimage_016():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 017")
def test_attach_smallimage_017():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 018")
def test_attach_smallimage_018():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 019")
def test_attach_smallimage_019():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 020")
def test_attach_smallimage_020():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 021")
def test_attach_smallimage_021():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 022")
def test_attach_smallimage_022():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 023")
def test_attach_smallimage_023():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 024")
def test_attach_smallimage_024():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 025")
def test_attach_smallimage_025():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 026")
def test_attach_smallimage_026():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 027")
def test_attach_smallimage_027():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 028")
def test_attach_smallimage_028():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 029")
def test_attach_smallimage_029():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 030")
def test_attach_smallimage_030():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 031")
def test_attach_smallimage_031():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 032")
def test_attach_smallimage_032():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 033")
def test_attach_smallimage_033():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 034")
def test_attach_smallimage_034():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 035")
def test_attach_smallimage_035():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 036")
def test_attach_smallimage_036():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 037")
def test_attach_smallimage_037():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 038")
def test_attach_smallimage_038():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 039")
def test_attach_smallimage_039():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 040")
def test_attach_smallimage_040():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 041")
def test_attach_smallimage_041():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 042")
def test_attach_smallimage_042():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 043")
def test_attach_smallimage_043():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 044")
def test_attach_smallimage_044():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 045")
def test_attach_smallimage_045():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 046")
def test_attach_smallimage_046():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 047")
def test_attach_smallimage_047():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 048")
def test_attach_smallimage_048():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 049")
def test_attach_smallimage_049():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 050")
def test_attach_smallimage_050():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 051")
def test_attach_smallimage_051():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 052")
def test_attach_smallimage_052():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 053")
def test_attach_smallimage_053():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 054")
def test_attach_smallimage_054():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 055")
def test_attach_smallimage_055():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 056")
def test_attach_smallimage_056():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 057")
def test_attach_smallimage_057():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 058")
def test_attach_smallimage_058():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 059")
def test_attach_smallimage_059():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 060")
def test_attach_smallimage_060():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 061")
def test_attach_smallimage_061():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 062")
def test_attach_smallimage_062():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 063")
def test_attach_smallimage_063():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 064")
def test_attach_smallimage_064():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 065")
def test_attach_smallimage_065():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 066")
def test_attach_smallimage_066():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 067")
def test_attach_smallimage_067():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 068")
def test_attach_smallimage_068():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 069")
def test_attach_smallimage_069():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 070")
def test_attach_smallimage_070():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 071")
def test_attach_smallimage_071():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 072")
def test_attach_smallimage_072():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 073")
def test_attach_smallimage_073():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 074")
def test_attach_smallimage_074():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 075")
def test_attach_smallimage_075():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 076")
def test_attach_smallimage_076():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 077")
def test_attach_smallimage_077():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 078")
def test_attach_smallimage_078():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 079")
def test_attach_smallimage_079():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 080")
def test_attach_smallimage_080():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 081")
def test_attach_smallimage_081():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 082")
def test_attach_smallimage_082():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 083")
def test_attach_smallimage_083():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 084")
def test_attach_smallimage_084():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 085")
def test_attach_smallimage_085():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 086")
def test_attach_smallimage_086():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 087")
def test_attach_smallimage_087():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 088")
def test_attach_smallimage_088():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 089")
def test_attach_smallimage_089():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 090")
def test_attach_smallimage_090():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 091")
def test_attach_smallimage_091():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 092")
def test_attach_smallimage_092():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 093")
def test_attach_smallimage_093():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 094")
def test_attach_smallimage_094():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 095")
def test_attach_smallimage_095():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 096")
def test_attach_smallimage_096():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 097")
def test_attach_smallimage_097():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 098")
def test_attach_smallimage_098():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 099")
def test_attach_smallimage_099():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 10 Kbytes attachment 100")
def test_attach_smallimage_100():

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
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 10 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 10 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("Sending normal 10 kbytes JPG attach"):
                allure.attach.file(os.path.join("resources", "small-image.jpg"), name="10 Kb JPG example", attachment_type=attachment_type.JPG)

