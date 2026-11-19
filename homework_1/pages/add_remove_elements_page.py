from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    URL = "http://the-internet.herokuapp.com/add_remove_elements/"

    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def click_add_element(self):
        self.click(self.ADD_BUTTON)
        return self

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTON)

    def get_delete_buttons_count(self) -> int:
        return len(self.get_delete_buttons())

    def click_delete_button(self, index: int = 0):
        buttons = self.wait.until(
            lambda d: d.find_elements(*self.DELETE_BUTTON)
        )
        buttons[index].click()
        return self