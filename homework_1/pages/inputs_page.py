from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class InputsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/inputs"
    INPUT = (By.TAG_NAME, "input")

    def get_input(self):
        return self.find(self.INPUT)

    def clear_input(self):
        self.get_input().clear()
        return self

    def type_value(self, value: str):
        self.get_input().send_keys(value)
        return self

    def press_arrow_up(self):
        self.get_input().send_keys(Keys.ARROW_UP)
        return self

    def press_arrow_down(self):
        self.get_input().send_keys(Keys.ARROW_DOWN)
        return self

    def get_value(self) -> str:
        return self.get_input().get_attribute("value")