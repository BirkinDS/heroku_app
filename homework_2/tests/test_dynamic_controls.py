import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from pages.dynamic_controls_page import DynamicControlsPage


@pytest.mark.smoke
def test_dynamic_controls(browser):
    page = DynamicControlsPage(browser).open()

    # 1. Удаляем чекбокс и ждём подтверждение от страницы.
    page.remove_checkbox()
    page.wait_message("It's gone!")
    page.wait.until(lambda driver: not page.checkbox_exists())
    assert not page.checkbox_exists(), "Чекбокс должен отсутствовать на странице"

    # 2. Проверяем, что поле ввода изначально неактивно.
    page.wait.until(lambda driver: not page.get_input().is_enabled())
    input_element = page.get_input()
    assert input_element.is_enabled() is False, (
        "Поле ввода до нажатия Enable должно быть неактивным. "
        f"Атрибут disabled: {input_element.get_attribute('disabled')!r}"
    )
    print("ПРОВЕРКА: поле ввода неактивно до нажатия Enable.")

    # 3. Включаем поле и проверяем, что оно стало активным.
    page.enable_input()
    page.wait_message("It's enabled!")
    page.wait.until(EC.element_to_be_clickable(page.INPUT))
    input_element = page.get_input()
    assert input_element.is_enabled() is True, (
        "После нажатия Enable поле должно стать активным"
    )
    print("ПРОВЕРКА: поле ввода стало активным.")

    # Небольшая пауза, чтобы можно было увидеть активное поле в браузере.
    time.sleep(1.5)

    # 4. Вводим текст и проверяем, что он появился в поле.
    input_element.send_keys("Привет")
    assert input_element.get_attribute("value") == "Привет", (
        "В поле ввода должен появиться текст 'Привет'"
    )
    print("ПРОВЕРКА: в активное поле введено слово 'Привет'.")
