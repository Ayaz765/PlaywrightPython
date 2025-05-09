
from utils.base_page import BasePage
from utils.config_reader import get_config

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page, get_config("paths", "locator_file"), ['login'])

    def perform_login(self, username, password):
        self.goto(get_config("urls", "base_url"))
        self.fill("username_field", username)
        self.fill("password_field", password)
        self.click("submit_button")
