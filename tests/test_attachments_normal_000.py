import json
import os

import allure
from allure import attachment_type


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_000():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_001():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_002():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_003():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_004():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_005():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_006():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_007():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_008():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_009():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_010():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_011():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_012():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_013():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_014():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_015():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_016():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_017():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_018():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_019():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_020():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_021():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_022():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_023():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_024():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_025():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_026():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_027():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_028():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_029():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_030():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_031():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_032():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_033():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_034():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_035():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_036():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_037():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_038():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_039():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_040():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_041():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_042():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_043():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_044():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_045():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_046():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_047():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_048():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_049():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_050():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_051():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_052():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_053():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_054():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_055():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_056():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_057():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_058():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_059():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_060():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_061():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_062():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_063():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_064():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_065():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_066():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_067():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_068():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_069():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_070():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_071():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_072():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_073():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_074():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_075():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_076():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_077():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_078():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_079():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_080():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_081():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_082():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_083():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_084():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_085():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_086():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_087():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_088():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_089():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_090():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_091():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_092():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_093():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_094():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_095():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_096():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_097():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_098():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_099():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 200+ Kbytes attachment")
def test_attach_normalimage_100():
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("txt attach"):
        allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
    with allure.step("CSV attach"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Sending normal 240 kbytes JPG attach"):
            allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("Sending normal 240 kbytes JPG attach"):
        allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


