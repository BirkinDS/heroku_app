import time
from pathlib import Path

import pytest

from pages.file_download_page import FileDownloadPage


@pytest.mark.regression
def test_file_download(browser, download_dir):
    print("\\nОткрываю страницу File Download...")
    page = FileDownloadPage(browser).open()

    print("\\nДОЙДИ ДО БРАУЗЕРА И САМОСТОЯТЕЛЬНО НАЖМИ НА ССЫЛКУ ФАЙЛА.")
    print("После нажатия тест автоматически проверит скачивание.")
    print(f"Папка загрузки: {Path(download_dir).resolve()}")

    deadline = time.monotonic() + 120
    downloaded_file = None

    while time.monotonic() < deadline:
        partial_downloads = list(Path(download_dir).glob("*.crdownload"))
        completed_files = [
            path for path in Path(download_dir).iterdir()
            if path.is_file() and not path.name.endswith(".crdownload")
        ]
        if completed_files and not partial_downloads:
            downloaded_file = max(completed_files, key=lambda path: path.stat().st_mtime)
            break
        time.sleep(0.5)

    assert downloaded_file is not None, (
        "Файл не появился в папке загрузок за 120 секунд. "
        "Убедись, что нажал ссылку скачивания в открытом браузере."
    )
    assert downloaded_file.stat().st_size > 0, "Скачанный файл пустой"

    print(f"ФАЙЛ УСПЕШНО СКАЧАН: {downloaded_file.resolve()}")
    print(f"Размер файла: {downloaded_file.stat().st_size} байт")
