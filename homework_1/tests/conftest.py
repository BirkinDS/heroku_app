import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    """Создаёт Chrome WebDriver перед тестом и закрывает после."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--incognito")   # можно включить при необходимости
    # options.add_argument("--headless")    # для CI

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()