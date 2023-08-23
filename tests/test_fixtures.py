import allure
import pytest

@allure.title("Fixture title")
@pytest.fixture
def titled_fixture():
    with allure.step("Step one will pass, testing fixture title"):
        pass
    with allure.step("Step two will pass, testing fixture title"):
        pass
    with allure.step("Step three will pass, testing fixture title"):
        pass


@allure.suite("Second steps")
@allure.feature("Testing fixtures")
@allure.story("Checking fixture title is present in Allure TestOps")
@allure.title("Fixture title should be present in the Execution")
def test_with_fixture_title(titled_fixture):
    with allure.step("Step will just pass, testing fixture title"):
        pass

@allure.title("Session level yield fixture")
@pytest.fixture(scope="session")
def session_level_yield_fixture():
    with allure.step("Step inside session level fixture"):
        pass

    yield

    with allure.step("Step inside finalizer session level fixture"):
        pass

@allure.title("Module level yield fixture")
@pytest.fixture(scope="module")
def module_level_yield_fixture():
    with allure.step("Step inside module level fixture"):
        pass

    yield

    with allure.step("Step inside finalizer module level fixture"):
        pass

@allure.title("Function level yield fixture")
@pytest.fixture
def function_level_yield_fixture():
    with allure.step("Step inside function level fixture"):
        pass

    yield

    with allure.step("Step inside finalizer function level fixture"):
        pass

@allure.title("Session level yield fixture")
@pytest.fixture(scope="session")
def session_level_fixture(request):
    with allure.step("Step inside session level fixture"):
        pass

    def finalizer():
        with allure.step("Step inside finalizer session level fixture"):
            pass

    request.addfinalizer(finalizer)


@pytest.fixture
def module_level_fixture(request):
    with allure.step("Step inside module level fixture"):
        pass

    def finalizer():
        with allure.step("Step inside finalizer module level fixture"):
            pass

    request.addfinalizer(finalizer)


@pytest.fixture
def function_level_fixture(request):
    with allure.step("Step inside function level fixture"):
        pass

    def finalizer():
        with allure.step("Step inside finalizer function level fixture"):
            pass

    request.addfinalizer(finalizer)


def test_allure_yield_fixture(session_level_yield_fixture, module_level_yield_fixture, function_level_yield_fixture):
    with allure.step("Step inside test_allure_yield_fixture"):
        pass


def test_allure_fixture_with_finalizer(session_level_fixture, module_level_fixture, function_level_fixture):
    with allure.step("Step inside test_allure_fixture_with_finalizer"):
        pass