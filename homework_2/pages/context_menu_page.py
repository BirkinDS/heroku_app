from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage


class ContextMenuPage(BasePage):
    URL = "https://the-internet.herokuapp.com/context_menu"
    HOT_SPOT = (By.ID, "hot-spot")

    def right_click_hot_spot(self):
        element = self.find(self.HOT_SPOT)
        ActionChains(self.driver).context_click(element).perform()
        return self
