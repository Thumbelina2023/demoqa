from pages.text_box import TextBox
import time

def test_text_clear(browser):
    text_b = TextBox(browser)
    text_b.visit()

    text_b.full_name.send_keys('I am')
    time.sleep(2)

    text_b.full_name.clear()
    time.sleep(2)

    assert text_b.full_name.get_text() == ''
