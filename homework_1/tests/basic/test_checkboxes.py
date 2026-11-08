import pytest

from pages.checkboxes_page import CheckboxesPage

@pytest.mark.smoke
def test_checkboxes(browser):
        page = CheckboxesPage(browser).open()
        # Шаг 1: первый чекбокс изначально unchecked
        first = page.get_first_checkbox()
        assert first.is_selected() is False, "Первый чекбокс должен быть unchecked"
        # Шаг 2: отмечаем первый чекбокс
        first.click()
        first = page.get_first_checkbox()
        assert first.is_selected() is True, "Первый чекбокс должен стать checked"
        # Шаг 3: второй чекбокс изначально checked
        second = page.get_second_checkbox()
        assert second.is_selected() is True, "Второй чекбокс должен быть checked"
        # Шаг 4: снимаем галочку со второго
        second.click()
        second = page.get_second_checkbox()
        assert second.is_selected() is False, "Второй чекбокс должен стать unchecked"