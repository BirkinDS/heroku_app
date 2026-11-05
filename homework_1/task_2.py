import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Задержка между шагами (в секундах), чтобы визуально наблюдать за тестом
STEP_DELAY = 1


class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def get_first_checkbox(self):
        return self.get_checkboxes()[0]

    def get_second_checkbox(self):
        return self.get_checkboxes()[1]


def test_checkboxes():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        page = CheckboxesPage(driver)

        # Шаг 1: открыть страницу Checkboxes
        print("Шаг 1: Открываем страницу Checkboxes")
        page.open()
        time.sleep(STEP_DELAY)

        # Шаг 2: проверить, что первый чекбокс unchecked
        print("Шаг 2: Проверяем, что первый чекбокс unchecked")
        first = page.get_first_checkbox()
        assert first.is_selected() is False, "Первый чекбокс должен быть unchecked"
        print("Первый чекбокс unchecked")
        time.sleep(STEP_DELAY)

        # Шаг 3: отметить первый чекбокс
        print("Шаг 3: Отмечаем первый чекбокс")
        first.click()
        time.sleep(STEP_DELAY)

        # Шаг 4: проверить, что первый чекбокс стал checked
        print("Шаг 4: Проверяем, что первый чекбокс стал checked")
        first = page.get_first_checkbox()
        assert first.is_selected() is True, "Первый чекбокс должен стать checked"
        print("Первый чекбокс стал checked")
        time.sleep(STEP_DELAY)

        # Шаг 5: проверить, что второй чекбокс checked
        print("Шаг 5: Проверяем, что второй чекбокс checked")
        second = page.get_second_checkbox()
        assert second.is_selected() is True, "Второй чекбокс должен быть checked"
        print("Второй чекбокс checked")
        time.sleep(STEP_DELAY)

        # Шаг 6: снять галочку со второго чекбокса (uncheck)
        print("Шаг 6: Снимаем галочку со второго чекбокса")
        second.click()
        time.sleep(STEP_DELAY)

        # Шаг 7: проверить, что второй чекбокс стал unchecked
        print("Шаг 7: Проверяем, что второй чекбокс стал unchecked")
        second = page.get_second_checkbox()
        assert second.is_selected() is False, "Второй чекбокс должен стать unchecked"
        print("Второй чекбокс стал unchecked")
        time.sleep(STEP_DELAY)

        print("Тест завершен")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkboxes()