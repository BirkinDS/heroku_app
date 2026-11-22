import pytest
from selenium.webdriver.common.alert import Alert
from pages.context_menu_page import ContextMenuPage


@pytest.mark.smoke
def test_context_menu(browser):
    page = ContextMenuPage(browser).open()
    page.right_click_hot_spot()
    alert = Alert(browser)
    assert alert.text == "You selected a context menu"
    alert.accept()
