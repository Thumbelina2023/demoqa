from pages.elements_page_2 import ElementsPage
from pages.demoqa import DemoQa

def test_check_text(browser):
    footer = ElementsPage(browser)
    btn = DemoQa(browser)
    text_centre = ElementsPage(browser)
    footer.visit()
    assert footer.footer_tx.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    btn.btn_elements.click()
    assert text_centre.text_c.get_text() == 'Please select an item from left to start practice.'
