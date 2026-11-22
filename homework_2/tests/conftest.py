from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOWNLOAD_DIR = PROJECT_ROOT / "downloads"

TASK_ORDER = {
    "test_context_menu.py": 1,
    "test_dynamic_controls.py": 2,
    "test_file_upload.py": 3,
    "test_frames.py": 4,
    "test_file_download.py": 5,
}

TASK_LABELS = {
    "test_context_menu.py": "Context Menu",
    "test_dynamic_controls.py": "Dynamic Controls",
    "test_file_upload.py": "File Upload",
    "test_frames.py": "Frames",
    "test_file_download.py": "File Download",
}


def pytest_collection_modifyitems(items):
    """Гарантирует запуск заданий строго от 1 до 5."""
    items.sort(
        key=lambda item: TASK_ORDER.get(Path(str(item.fspath)).name, 999)
    )


def pytest_runtest_logreport(report):
    """Печатает итоговую строку по заданию после завершения теста."""
    if report.when != "teardown":
        return

    filename = Path(report.location[0]).name
    if filename not in TASK_LABELS:
        return

    # Для одного теста report teardown содержит статус teardown;
    # ошибки setup/call pytest отражает в соответствующих report.
    # Сохраняем статусы всех фаз между вызовами hook.
    failed = getattr(report, "_homework_failed", report.failed)
    number = TASK_ORDER[filename]
    title = TASK_LABELS[filename]
    status = "неуспешно (FAILED)" if failed else "успешно (PASSED)"
    print(f"ЗАДАНИЕ {number}/5 - {status} - {title}", flush=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    reports = getattr(item, "_homework_reports", [])
    reports.append(report)
    item._homework_reports = reports
    if report.when == "teardown":
        # Итоговый статус сохраняем на report для итогового hook.
        report._homework_failed = any(r.failed for r in reports)


@pytest.fixture(scope="function")
def download_dir():
    """Постоянная папка: скачанные файлы остаются после завершения теста."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    return DOWNLOAD_DIR


@pytest.fixture(scope="function")
def browser(download_dir):
    """Создаёт Chrome с постоянной директорией загрузок для homework_2."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "download.default_directory": str(download_dir.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
