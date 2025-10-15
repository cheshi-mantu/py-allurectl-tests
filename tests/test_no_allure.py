import allure

@allure.feature("Stored scenario")
@allure.story("We have 10k tests")
@allure.title("Ty menya trololo without allure?")
def test_passing_noallure():
    assert (1, 2, 3) == (1, 2, 3)


@allure.feature("Stored scenario")
@allure.story("We have 10k tests")
@allure.title("Ty menya trololo with allure?")
def test_passing_with_allure():
    with allure.step("assert (1, 2, 3) == (1, 2, 3)"):
        assert (1, 2, 3) == (1, 2, 3)
