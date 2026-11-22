import pytest
from pages.frames_page import FramesPage


@pytest.mark.smoke
def test_frames(browser):
    page = FramesPage(browser).open()
    page.switch_to_frame()
    assert page.get_frame_text() == "Your content goes here."
    page.switch_to_default_content()
    assert browser.switch_to.active_element is not None
