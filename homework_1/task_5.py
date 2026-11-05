import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Задержка между шагами (в секундах), чтобы визуально наблюдать за тестом
STEP_DELAY = 1


class TyposPage:

    URL = "https://the-internet.herokuapp.com/typos"
    PARAGRAPH = (By.TAG_NAME, "p")

    # Эталонный правильный текст
    CORRECT_TEXT = "Sometimes you'll see a typo, other times you won't."

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def refresh(self):
        self.driver.refresh()

    def get_paragraphs(self):
        return self.driver.find_elements(*self.PARAGRAPH)

    def get_second_paragraph_text(self):
        return self.get_paragraphs()[1].text


def find_first_difference(expected, actual):
    """Возвращает описание первого расхождения между expected и actual."""
    min_len = min(len(expected), len(actual))
    for i in range(min_len):
        if expected[i] != actual[i]:
            return (
                f"позиция {i}: ожидалось '{expected[i]}', "
                f"получено '{actual[i]}'"
            )
    if len(expected) != len(actual):
        return (
            f"длина: ожидалось {len(expected)} символов, "
            f"получено {len(actual)} символов"
        )
    return "расхождений не найдено"


def test_typos():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        page = TyposPage(driver)

        # Шаг 1: открыть страницу Typos
        print("Шаг 1: Открываем страницу Typos")
        page.open()
        time.sleep(STEP_DELAY)

        # Шаг 2: проверить текст параграфа на 10 обновлениях
        print("Шаг 2: Проверяем текст параграфа на 10 обновлениях страницы")
        print(f"Эталонный текст: '{page.CORRECT_TEXT}'")
        typo_attempts = []
        correct_attempts = []

        for i in range(1, 11):
            text = page.get_second_paragraph_text()

            if text == page.CORRECT_TEXT:
                print(f"Попытка {i}: текст совпадает с эталоном")
                correct_attempts.append(i)
            else:
                print(f"Попытка {i}: текст НЕ совпадает с эталоном")
                print(f"  Ожидалось: '{page.CORRECT_TEXT}'")
                print(f"  Получено:  '{text}'")
                print(f"  Расхождение: {find_first_difference(page.CORRECT_TEXT, text)}")
                typo_attempts.append(i)

            time.sleep(STEP_DELAY)
            page.refresh()
            time.sleep(STEP_DELAY)

        # Шаг 3: вывести итог
        print("Шаг 3: Выводим итог по попыткам")
        print(f"Попыток без опечатки: {len(correct_attempts)}")
        print(f"Попыток с опечаткой: {len(typo_attempts)}")
        if typo_attempts:
            print(f"Опечатка встретилась на попытках: {typo_attempts}")
        else:
            print("За 10 обновлений опечатка не отобразилась")

        # Шаг 4: проверить, что текст не пустой
        print("Шаг 4: Проверяем, что текст параграфа не пустой")
        final_text = page.get_second_paragraph_text()
        assert final_text != "", "Текст второго параграфа не должен быть пустым"
        print(f"Текущий текст параграфа: '{final_text}'")
        time.sleep(STEP_DELAY)

        print("Тест завершен")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_typos()