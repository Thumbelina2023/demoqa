from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    navigation = DemoQa(browser)
    nav = ElementsPage(browser)
    navigation.visit()
    navigation.btn_elements.click()
    navigation.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    nav.equal_url()
    assert nav.equal_url()
