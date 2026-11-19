import pytest

from pages.add_remove_elements_page import AddRemoveElementsPage


@pytest.mark.smoke
def test_add_remove_elements(browser):
    page = AddRemoveElementsPage(browser).open()
    # Добавляем 2 кнопки DELETE
    page.click_add_element().click_add_element()
    assert page.get_delete_buttons_count() == 2, "Ожидалось 2 кнопки Delete"
    # Удаляем первую - остаётся одна
    page.click_delete_button(index=0)
    assert page.get_delete_buttons_count() == 1, "Ожидалась 1 кнопка Delete"