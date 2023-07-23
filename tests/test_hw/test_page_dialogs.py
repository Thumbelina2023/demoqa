from pages.modal_dialogs import modal_dialogs
import time


def test_modal_elements(browser):
    modal_element = modal_dialogs(browser)
    modal_element.visit()
    modal_element.btn_modal_dialog.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_navigation = modal_dialogs(browser)
    modal_navigation.visit()
    browser.refresh()
    modal_navigation.icon.click()
    browser.back()
    browser.set_window_size(900,400)
    browser.forward()
    assert modal_navigation.get_url() == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000,1000)
    time.sleep(3)
