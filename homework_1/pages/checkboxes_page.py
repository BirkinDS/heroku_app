from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")

    def get_checkboxes(self):
        return self.find_all(self.CHECKBOXES)

    def get_first_checkbox(self):
        return self.get_checkboxes()[0]

    def get_second_checkbox(self):
        return self.get_checkboxes()[1]