from pages.elements_page import ElementsPage


def test_find_elements(browser):
    elem = ElementsPage(browser)
    elem.visit()
    assert elem.btn_elem.check_count_elements (count=9)
