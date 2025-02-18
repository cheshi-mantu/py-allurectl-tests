import allure

@allure.feature("Answering questions")
@allure.story("Answering questionable questions")
@allure.title("Do stuff and then assert dammit")
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
        pass
        with allure.step("asserting 2 > 3"):
            assert(2 > 3)