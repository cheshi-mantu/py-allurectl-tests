import allure

@allure.suite("cloud instance")
@allure.feature("sending attachments")
@allure.story("sending JSON attachments")
@allure.title("Sending JSON attachments")
def test_json_attach():
    with allure.step("define stuff"):
        pass
    with allure.step("expected result 2 > 3"):
        assert(2 > 3)