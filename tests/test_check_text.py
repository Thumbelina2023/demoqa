from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_page_elements(browser):
    t_p_e = ElementsPage(browser)
    t_p_e.visit()
    assert t_p_e.tx.get_text() == 'Elements'

    assert t_p_e.icon.exist()
    assert t_p_e.said_bar.exist()
    assert t_p_e.said_bar_textbox.exist()