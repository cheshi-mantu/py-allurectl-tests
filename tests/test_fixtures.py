import pytest
import os
import allure
from allure import attachment_type


@allure.title("Fixture with attachments only")
@pytest.fixture
def titled_fixture():
    # with allure.step("Step one will pass, testing fixture title"):
    allure.attach.file(os.path.join("resources", "normal-image.jpg"), name="240 Kb JPG example", attachment_type=attachment_type.JPG)
    pass
    # with allure.step("Step two will pass, testing fixture title"):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)

    # with allure.step("Step three will pass, testing fixture title"):
    #     allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)
    #     pass
    allure.attach("<h1>Example html attachment</h1>", name="HTML example", attachment_type=attachment_type.HTML)


@allure.suite("Second steps")
@allure.feature("Testing fixtures")
@allure.story("Checking fixture title is present in Allure TestOps")
@allure.title("Fixture title should be present in the Execution")
def test_with_fixture_title(titled_fixture):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    pass

@allure.title("Session level yield fixture")
@pytest.fixture(scope="session")
def session_level_yield_fixture():
    with allure.step("Step inside session level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass

    yield

    with allure.step("Step inside finalizer session level fixture"):
        pass

@allure.title("Module level yield fixture")
@pytest.fixture(scope="module")
def module_level_yield_fixture():
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside module level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass

    yield
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside finalizer module level fixture"):
        pass

@allure.title("Function level yield fixture")
@pytest.fixture
def function_level_yield_fixture():
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside function level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass
    yield
    with allure.step("Step inside finalizer function level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        # raise allure.BrokenException("Forcing test to be marked as BROKEN")
        pass

@allure.title("Session level yield fixture")
@pytest.fixture(scope="session")
def session_level_fixture(request):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside session level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass

    def finalizer():
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Step inside finalizer session level fixture"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
            pass

    request.addfinalizer(finalizer)


@pytest.fixture
def module_level_fixture(request):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside module level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass

    def finalizer():
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Step inside finalizer module level fixture"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
            pass

    request.addfinalizer(finalizer)


@pytest.fixture
def function_level_fixture(request):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside function level fixture"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass

    def finalizer():
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        with allure.step("Step inside finalizer function level fixture"):
            allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
            pass

    request.addfinalizer(finalizer)


def test_allure_yield_fixture(session_level_yield_fixture, module_level_yield_fixture, function_level_yield_fixture):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside test_allure_yield_fixture"):
        # raise allure.BrokenException("Forcing test to be marked as BROKEN")
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass


def test_allure_fixture_with_finalizer(session_level_fixture, module_level_fixture, function_level_fixture):
    allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
    with allure.step("Step inside test_allure_fixture_with_finalizer"):
        allure.attach('first,second,third\none,two,three', name="CSV example", attachment_type=attachment_type.CSV)
        pass