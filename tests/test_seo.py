from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_seo(browser):
    seo = DemoQa(browser)

    seo.visit()
    assert browser.title == 'DEMOQA'