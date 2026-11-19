from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def get_select(self) -> Select:
        return Select(self.find(self.DROPDOWN))