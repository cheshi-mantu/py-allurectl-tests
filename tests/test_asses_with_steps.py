import allure

@allure.suite("cloud instance")
@allure.feature("sending attachments")
@allure.story("sending JSON attachments")
@allure.title("Sending JSON attachments")
def test_json_attach():
    with allure.step("define stuff"):
        pass
    with allure.step("define stuff"):
        pass
    with allure.step("do stuff"):
        pass
    with allure.step("do more stuff"):
        pass
    with allure.step("do even more stuff"):
        pass
    with allure.step("expected result 2 > 3"):
        assert(2 > 3)