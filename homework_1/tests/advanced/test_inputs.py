import pytest

from pages.inputs_page import InputsPage


@pytest.mark.regression
def test_inputs(browser):
    page = InputsPage(browser).open()
    # Ввод цифрового значения
    page.type_value("2")
    assert page.get_value() == "2"
    # ARROW_UP → 3
    page.press_arrow_up()
    assert page.get_value() == "3"
    # ARROW_DOWN → 2
    page.press_arrow_down()
    assert page.get_value() == "2"
    # Нецифровое значение не принимается
    page.clear_input().type_value("abc")
    assert page.get_value() == "", "Поле должно остаться пустым после ввода 'abc'"
    # ARROW_UP на пустом поле → 1
    page.press_arrow_up()
    assert page.get_value() == "1"
    # ARROW_DOWN → 0
    page.press_arrow_down()
    assert page.get_value() == "0"