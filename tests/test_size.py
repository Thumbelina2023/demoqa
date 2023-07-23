from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time
def test_size(browser):
    size = DemoQa(browser)
    size.visit()
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)

def test_visible_nav_bar(browser):
    nav_bar = ElementsPage(browser)
    nav_bar.visit()
    assert not nav_bar.elem_nav.visible()
    nav_bar.elem_nav.set_window_size(600,660)
    assert nav_bar.elem_nav.visible()
    browser.set_window_size(1000,1000)
