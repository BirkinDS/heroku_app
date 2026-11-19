from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TyposPage(BasePage):
    URL = "https://the-internet.herokuapp.com/typos"
    PARAGRAPH = (By.TAG_NAME, "p")

    CORRECT_TEXT = "Sometimes you'll see a typo, other times you won't."

    def refresh(self):
        self.driver.refresh()
        return self

    def get_paragraphs(self):
        return self.driver.find_elements(*self.PARAGRAPH)

    def get_second_paragraph_text(self) -> str:
        return self.get_paragraphs()[1].text