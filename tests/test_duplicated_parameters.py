import allure

@allure.epic("Uploader")
@allure.feature("Reliability")
@allure.story("Duplicated parameter")
@allure.title("Uploader should correctly process duplicated keys in test results")
def test_should_not_fail_on_duplicated_params():
    allure.dynamic.parameter("uno", "uno-uno", excluded=None, mode=None)
    allure.dynamic.parameter("dos", "dos-dos", excluded=None, mode=None)
    allure.dynamic.parameter("uno", "uno-dos", excluded=None, mode=None)