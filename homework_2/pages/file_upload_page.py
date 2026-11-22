from selenium.webdriver.common.by import By
from .base_page import BasePage


class FileUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE = (By.ID, "uploaded-files")

    def upload_file(self, file_path):
        self.find(self.FILE_INPUT).send_keys(str(file_path))
        self.click(self.UPLOAD_BUTTON)
        return self

    def get_uploaded_filename(self) -> str:
        return self.find(self.UPLOADED_FILE).text
