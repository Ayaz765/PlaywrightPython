
import pytest
from utils.excelReader import read_test_data
from utils.config_reader import get_config
from pages.login import LoginPage

test_data = read_test_data(get_config("paths", "excel_file"), "login")

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.login_page = LoginPage(page)

    @pytest.mark.smoke
    @pytest.mark.parametrize("serial,username,password,email", test_data)
    def test_account_creation(self, serial, username, password, email):
        self.login_page.perform_login(username, password)
