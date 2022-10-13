import pytest


@pytest.fixture(scope="class")
def admin_client():
    yield "admin"
    print("Tear down admin")


@pytest.fixture(scope="class")
def user(admin_client):
    _user = "Susan"
    yield _user
    print("Tear down User")


@pytest.fixture(scope="class")
def driver():
    _driver = "driver"
    yield _driver
    print("Driver tear down")


@pytest.fixture(scope="class")
def landing_page(driver):
    return driver


class TestLandingPageSuccess:
    value = ""
    key = "A"

    @pytest.fixture(scope="class", autouse=True)
    def login(self, driver, admin_client, user):
        value = "\n auto use fixture"
        print(driver, admin_client, user, value)
        print("end of login fixture load")

    @pytest.mark.skip
    def test_name_in_header(self, user):
        print(self.value)
        assert True

    def test_sign_out_button(self, driver):
        print(self.value)
        assert True

    def test_profile_link(self, admin_client):
        print(self.value)
        assert True

    def test_raises_bad_credentials_exception(self, user):
        with pytest.raises(BadCredentialsException):
            assert True
