from pages.text_box import TextBox
import time

def test_text_box(browser):
    tex_box = TextBox(browser)
    tex_box.visit()
    tex_box.full_name.send_keys('Ivan Pupkin')
    tex_box.current_address.send_keys('SPb')
    tex_box.btn_submit.click()
    time.sleep(6)

    assert tex_box.full_name_assert.get_text() == 'Name:' + 'Ivan Pupkin'
    assert tex_box.current_address_assert.get_text() == 'Current Address :' + 'SPb'





