import pytest
from pages.file_upload_page import FileUploadPage


@pytest.mark.smoke
def test_file_upload(browser, tmp_path):
    file_name = "selenium_test_upload.txt"
    file_path = tmp_path / file_name
    file_path.write_text("Тестовый файл для домашнего задания Selenium.", encoding="utf-8")

    page = FileUploadPage(browser).open()
    page.upload_file(file_path)

    assert page.get_uploaded_filename() == file_name
