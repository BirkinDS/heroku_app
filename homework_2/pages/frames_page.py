from selenium.webdriver.common.by import By
from .base_page import BasePage


class FramesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/iframe"
    FRAME = (By.ID, "mce_0_ifr")
    FRAME_TEXT = (By.ID, "tinymce")

    def switch_to_frame(self):
        frame = self.find(self.FRAME)
        self.driver.switch_to.frame(frame)
        return self

    def get_frame_text(self) -> str:
        return self.find(self.FRAME_TEXT).text

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        return self
