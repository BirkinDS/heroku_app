import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Задержка между шагами (в секундах), чтобы визуально наблюдать за тестом
STEP_DELAY = 2


class DropdownPage:

    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_select(self):
        return Select(self.driver.find_element(*self.DROPDOWN))


def test_dropdown():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        page = DropdownPage(driver)

        # Шаг 1: открыть страницу Dropdown
        print("Шаг 1: Открываем страницу Dropdown")
        page.open()
        time.sleep(STEP_DELAY)

        # Шаг 2: получить все элементы дропдауна и проверить их наличие
        print("Шаг 2: Получаем все элементы дропдауна и проверяем их наличие")
        select = page.get_select()
        all_options = select.options
        assert len(all_options) > 0, "В дропдауне нет вариантов"
        print(f"Найдено вариантов: {len(all_options)}")
        for option in all_options:
            print(f"Вариант: '{option.text}'")
        time.sleep(STEP_DELAY)

        # Шаг 3: выбрать первый доступный вариант
        # Индекс 0 - плейсхолдер "Please select an option", индекс 1 - первый реальный вариант
        print("Шаг 3: Выбираем первый доступный вариант")
        select.select_by_index(1)
        time.sleep(STEP_DELAY)

        # Шаг 4: проверить, что выбран первый вариант
        print("Шаг 4: Проверяем, что выбран первый вариант")
        assert select.first_selected_option.text == "Option 1", \
            f"Ожидался 'Option 1', получен '{select.first_selected_option.text}'"
        print("Выбран Option 1")
        time.sleep(STEP_DELAY)

        # Шаг 5: выбрать второй вариант
        print("Шаг 5: Выбираем второй вариант")
        select.select_by_index(2)
        time.sleep(STEP_DELAY)

        # Шаг 6: проверить, что выбран второй вариант
        print("Шаг 6: Проверяем, что выбран второй вариант")
        assert select.first_selected_option.text == "Option 2", \
            f"Ожидался 'Option 2', получен '{select.first_selected_option.text}'"
        print("Выбран Option 2")
        time.sleep(STEP_DELAY)

        print("Тест завершен")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dropdown()