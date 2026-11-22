from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class DynamicControlsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"
    REMOVE_BUTTON = (By.XPATH, "//button[normalize-space()='Remove']")
    ENABLE_BUTTON = (By.XPATH, "//button[normalize-space()='Enable']")
    CHECKBOX = (By.CSS_SELECTOR, "#checkbox input")
    INPUT = (By.CSS_SELECTOR, "#input-example input[type='text']")
    MESSAGE = (By.ID, "message")

    def remove_checkbox(self):
        self.click(self.REMOVE_BUTTON)
        return self

    def wait_message(self, expected_text: str):
        self.wait.until(EC.text_to_be_present_in_element(self.MESSAGE, expected_text))
        return self

    def checkbox_exists(self) -> bool:
        return bool(self.driver.find_elements(*self.CHECKBOX))

    def get_input(self):
        return self.find(self.INPUT)

    def enable_input(self):
        self.click(self.ENABLE_BUTTON)
        return self
