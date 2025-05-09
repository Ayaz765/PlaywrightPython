import pandas as pd
from utils.logger import Logger

class BasePage:
    def __init__(self, page, file_path, sheets):
        self.page = page
        self.logger = Logger(__name__).get_logger()
        try:
            self.locators = self.load_locators(file_path, sheets)
            self.logger.info("Locators successfully loaded from Excel sheets.")
        except Exception as e:
            self.logger.error(f"Failed to load locators: {e}")
            raise

    def load_locators(self, file_path, sheets):
        all_locators = {}
        for sheet in sheets:
            try:
                locators = self.read_locators_from_sheet(file_path, sheet)
                self.logger.info(f"Loaded locators from sheet: {sheet}")
                all_locators.update(locators)
            except Exception as e:
                self.logger.error(f"Error reading sheet '{sheet}': {e}")
                raise
        return all_locators

    def read_locators_from_sheet(self, file_path, sheet_name):
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        locators = {}
        for index, row in df.iterrows():
            try:
                locators[row['Element Name']] = row['Locator']
            except KeyError as e:
                self.logger.warning(f"Missing expected column in sheet '{sheet_name}': {e}")
                raise
        return locators

    def goto(self, url):
        try:
            self.logger.info(f"Navigating to URL: {url}")
            self.page.goto(url)
        except Exception as e:
            self.logger.error(f"Failed to navigate to {url}: {e}")
            raise

    def fill(self, element_name, value):
        selector = self.locators.get(element_name)
        if selector:
            try:
                self.logger.info(f"Filling '{element_name}' with value: {value}")
                self.page.fill(selector, value)
            except Exception as e:
                self.logger.error(f"Failed to fill '{element_name}': {e}")
                raise
        else:
            self.logger.error(f"Locator for '{element_name}' not found")
            raise ValueError(f"Locator for {element_name} not found")

    def click(self, element_name):
        selector = self.locators.get(element_name)
        if selector:
            try:
                self.logger.info(f"Clicking on '{element_name}'")
                self.page.click(selector)
            except Exception as e:
                self.logger.error(f"Failed to click '{element_name}': {e}")
                raise
        else:
            self.logger.error(f"Locator for '{element_name}' not found")
            raise ValueError(f"Locator for {element_name} not found")

    def is_visible(self, element_name):
        selector = self.locators.get(element_name)
        if selector:
            try:
                visible = self.page.is_visible(selector)
                self.logger.info(f"Element '{element_name}' visibility: {visible}")
                return visible
            except Exception as e:
                self.logger.error(f"Failed to check visibility of '{element_name}': {e}")
                raise
        else:
            self.logger.error(f"Locator for '{element_name}' not found")
            raise ValueError(f"Locator for {element_name} not found")
