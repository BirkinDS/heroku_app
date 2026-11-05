import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Задержка между шагами (в секундах), чтобы визуально наблюдать за тестом
STEP_DELAY = 2


class InputsPage:

    URL = "https://the-internet.herokuapp.com/inputs"
    INPUT = (By.TAG_NAME, "input")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_input(self):
        return self.driver.find_element(*self.INPUT)

    def clear_input(self):
        self.get_input().clear()

    def type_value(self, value):
        self.get_input().send_keys(value)

    def press_arrow_up(self):
        self.get_input().send_keys(Keys.ARROW_UP)

    def press_arrow_down(self):
        self.get_input().send_keys(Keys.ARROW_DOWN)

    def get_value(self):
        return self.get_input().get_attribute("value")


def test_inputs():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        page = InputsPage(driver)

        # Шаг 1: открыть страницу Inputs
        print("Шаг 1: Открываем страницу Inputs")
        page.open()
        time.sleep(STEP_DELAY)

        # Шаг 2: ввести цифровое значение
        print("Шаг 2: Вводим цифровое значение '2'")
        page.type_value("2")
        assert page.get_value() == "2", f"Ожидалось '2', получено '{page.get_value()}'"
        print(f"Ввели: {page.get_value()}")
        time.sleep(STEP_DELAY)

        # Шаг 3: нажать ARROW_UP - значение должно увеличиться
        print("Шаг 3: Нажимаем ARROW_UP")
        page.press_arrow_up()
        assert page.get_value() == "3", f"Ожидалось '3', получено '{page.get_value()}'"
        print(f"После ARROW_UP: {page.get_value()}")
        time.sleep(STEP_DELAY)

        # Шаг 4: нажать ARROW_DOWN - значение должно уменьшиться
        print("Шаг 4: Нажимаем ARROW_DOWN")
        page.press_arrow_down()
        assert page.get_value() == "2", f"Ожидалось '2', получено '{page.get_value()}'"
        print(f"После ARROW_DOWN: {page.get_value()}")
        time.sleep(STEP_DELAY)

        # Шаг 5: очистить поле и ввести нецифровое значение
        print("Шаг 5: Очищаем поле и вводим нецифровое значение 'abc'")
        page.clear_input()
        page.type_value("abc")
        assert page.get_value() == "", f"Ожидаем пустую строку, получено '{page.get_value()}'"
        print(f"После ввода 'abc' значение: '{page.get_value()}'")
        time.sleep(STEP_DELAY)

        # Шаг 6: нажать ARROW_UP на пустом поле
        print("Шаг 6: Нажимаем ARROW_UP на пустом поле")
        page.press_arrow_up()
        assert page.get_value() == "1", f"Ожидалось '1', получено '{page.get_value()}'"
        print(f"После ARROW_UP на пустом поле: {page.get_value()}")
        time.sleep(STEP_DELAY)

        # Шаг 7: нажать ARROW_DOWN - значение должно вернуться к 0
        print("Шаг 7: Нажимаем ARROW_DOWN")
        page.press_arrow_down()
        assert page.get_value() == "0", f"Ожидалось '0', получено '{page.get_value()}'"
        print(f"После ARROW_DOWN: {page.get_value()}")
        time.sleep(STEP_DELAY)

        print("Тест завершен")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_inputs()