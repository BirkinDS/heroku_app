import pytest

from pages.dropdown_page import DropdownPage


@pytest.mark.smoke
@pytest.mark.parametrize(
    "index, expected_text",
    [
        (1, "Option 1"),
        (2, "Option 2"),
    ],
    ids=["option_1", "option_2"],
)
def test_dropdown(browser, index, expected_text):
    page = DropdownPage(browser).open()
    select = page.get_select()

    assert len(select.options) > 0, "В дропдауне нет вариантов"

    select.select_by_index(index)
    actual = select.first_selected_option.text
    assert actual == expected_text, f"Ожидался '{expected_text}', получен '{actual}'"