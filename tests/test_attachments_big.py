import json
import os
import time

import allure
from allure import attachment_type

@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 000")
def test_attach_bigimage_000():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 001")
def test_attach_bigimage_001():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 002")
def test_attach_bigimage_002():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 003")
def test_attach_bigimage_003():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 004")
def test_attach_bigimage_004():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 005")
def test_attach_bigimage_005():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 006")
def test_attach_bigimage_006():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 007")
def test_attach_bigimage_007():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 008")
def test_attach_bigimage_008():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 009")
def test_attach_bigimage_009():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 010")
def test_attach_bigimage_010():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 011")
def test_attach_bigimage_011():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 012")
def test_attach_bigimage_012():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 013")
def test_attach_bigimage_013():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 014")
def test_attach_bigimage_014():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 015")
def test_attach_bigimage_015():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 016")
def test_attach_bigimage_016():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 017")
def test_attach_bigimage_017():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 018")
def test_attach_bigimage_018():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 019")
def test_attach_bigimage_019():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 020")
def test_attach_bigimage_020():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 021")
def test_attach_bigimage_021():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 022")
def test_attach_bigimage_022():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 023")
def test_attach_bigimage_023():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 024")
def test_attach_bigimage_024():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 025")
def test_attach_bigimage_025():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 026")
def test_attach_bigimage_026():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 027")
def test_attach_bigimage_027():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 028")
def test_attach_bigimage_028():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 029")
def test_attach_bigimage_029():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 030")
def test_attach_bigimage_030():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 031")
def test_attach_bigimage_031():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 032")
def test_attach_bigimage_032():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 033")
def test_attach_bigimage_033():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 034")
def test_attach_bigimage_034():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 035")
def test_attach_bigimage_035():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 036")
def test_attach_bigimage_036():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 037")
def test_attach_bigimage_037():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 038")
def test_attach_bigimage_038():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 039")
def test_attach_bigimage_039():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 040")
def test_attach_bigimage_040():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 041")
def test_attach_bigimage_041():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 042")
def test_attach_bigimage_042():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 043")
def test_attach_bigimage_043():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 044")
def test_attach_bigimage_044():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 045")
def test_attach_bigimage_045():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 046")
def test_attach_bigimage_046():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 047")
def test_attach_bigimage_047():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 048")
def test_attach_bigimage_048():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 049")
def test_attach_bigimage_049():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 050")
def test_attach_bigimage_050():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 051")
def test_attach_bigimage_051():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 052")
def test_attach_bigimage_052():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 053")
def test_attach_bigimage_053():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 054")
def test_attach_bigimage_054():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 055")
def test_attach_bigimage_055():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 056")
def test_attach_bigimage_056():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 057")
def test_attach_bigimage_057():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 058")
def test_attach_bigimage_058():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 059")
def test_attach_bigimage_059():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 060")
def test_attach_bigimage_060():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 061")
def test_attach_bigimage_061():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 062")
def test_attach_bigimage_062():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 063")
def test_attach_bigimage_063():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 064")
def test_attach_bigimage_064():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 065")
def test_attach_bigimage_065():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 066")
def test_attach_bigimage_066():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 067")
def test_attach_bigimage_067():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 068")
def test_attach_bigimage_068():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 069")
def test_attach_bigimage_069():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 070")
def test_attach_bigimage_070():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 071")
def test_attach_bigimage_071():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 072")
def test_attach_bigimage_072():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 073")
def test_attach_bigimage_073():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 074")
def test_attach_bigimage_074():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 075")
def test_attach_bigimage_075():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 076")
def test_attach_bigimage_076():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 077")
def test_attach_bigimage_077():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 078")
def test_attach_bigimage_078():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 079")
def test_attach_bigimage_079():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 080")
def test_attach_bigimage_080():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 081")
def test_attach_bigimage_081():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 082")
def test_attach_bigimage_082():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 083")
def test_attach_bigimage_083():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 084")
def test_attach_bigimage_084():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 085")
def test_attach_bigimage_085():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 086")
def test_attach_bigimage_086():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 087")
def test_attach_bigimage_087():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 088")
def test_attach_bigimage_088():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 089")
def test_attach_bigimage_089():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 090")
def test_attach_bigimage_090():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 091")
def test_attach_bigimage_091():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 092")
def test_attach_bigimage_092():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 093")
def test_attach_bigimage_093():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 094")
def test_attach_bigimage_094():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 095")
def test_attach_bigimage_095():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 096")
def test_attach_bigimage_096():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 097")
def test_attach_bigimage_097():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 098")
def test_attach_bigimage_098():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 099")
def test_attach_bigimage_099():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


@allure.suite("cloud instance")
@allure.story("smoking pytest")
@allure.feature("sending attachments")
@allure.title("Sending 8 Mb JPG attachments 100")
def test_attach_bigimage_100():
    with allure.step("Sending big 8 megabytes JPG attach"):
        allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
        with allure.step("HTML attach"):
            allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
        with allure.step("CSV attach"):
            allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
    with allure.step("JSON attach"):
        allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
        with allure.step("URI list attach"):        
            allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
            with allure.step("Sending big 8 megabytes JPG attach"):
                allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
    with allure.step("HTML attach"):
        allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
        with allure.step("txt attach"):
            allure.attach("Some text content", name="TXT example", attachment_type=attachment_type.TEXT)
            with allure.step("CSV attach"):
                allure.attach.file(os.path.join("resources", "big-table.csv"), name="9,2 Mb CSV example", attachment_type=attachment_type.CSV)
                with allure.step("JSON attach"):
                    allure.attach(json.dumps({"first": 1, "second": 2}, indent=2),name="JSON example", attachment_type=attachment_type.JSON)
    with allure.step("URI list attach"):        
        allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)
        with allure.step("Sending big 8 megabytes JPG attach"):
            allure.attach.file(os.path.join("resources", "big-image.jpg"), name="8Mb JPG example", attachment_type=attachment_type.JPG)
            with allure.step("URI list attach"):        
                allure.attach("\n".join(["https://github.com/allure-framework", "https://github.com/allure-examples"]), name="URI List example", attachment_type=attachment_type.URI_LIST)


