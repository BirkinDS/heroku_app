import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Добавил задержку перед каждым шагом, чтобы визуально смотреть как проходит тест
STEP_DELAY = 1


class AddRemoveElementsPage:
    URL = "http://the-internet.herokuapp.com/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_add_element(self):
        self.driver.find_element(*self.ADD_BUTTON).click()

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.DELETE_BUTTON)


def test_add_remove_elements():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        page = AddRemoveElementsPage(driver)

        # Шаг 1: открыть страницу
        print("Открываем страницу add_remove_elements.")
        page.open()
        time.sleep(STEP_DELAY)

        # Шаг 2: добавить первый элемент
        print("Добавляем 1-й элемент.")
        page.click_add_element()
        time.sleep(STEP_DELAY)

        # Шаг 3: добавить второй элемент
        print("Добавляем 2-й элемент.")
        page.click_add_element()
        time.sleep(STEP_DELAY)

        # Шаг 4: проверить, что добавилось 2 кнопки DELETE
        buttons = page.get_delete_buttons()
        assert len(buttons) == 2
        print(f"Добавили 2 кнопки DELETE.")
        time.sleep(STEP_DELAY)

        # Шаг 5: удалить первый элемент
        print("Удаляем 1-й элемент.")
        buttons[0].click()
        time.sleep(STEP_DELAY)

        # Шаг 6: проверить, что осталась 1 кнопка DELETE
        buttons_after = page.get_delete_buttons()
        assert len(buttons_after) == 1
        print(f"Удалили 1 кнопку. Проверили что осталась одна кнопка DELETE: {len(buttons_after)}")
        time.sleep(STEP_DELAY)

        print("Тест завершен.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_add_remove_elements()
