from selenium.webdriver.common.by import By
from .base_page import BasePage


class FileDownloadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/download"
    FILE_LINKS = (By.CSS_SELECTOR, "div.example a")

    def get_file_links(self):
        return self.find_all(self.FILE_LINKS)

    def download_first_file(self) -> str:
        link = self.get_file_links()[0]
        filename = link.text.strip()
        link.click()
        return filename
