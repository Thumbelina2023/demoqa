
from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    btn = ElementsPage(browser)
    btn.visit()
    #btn.said_bar.click()
    #assert btn.said_bar_textbox.exist() заменили на визибл
    assert btn.said_bar_textbox.visible() # проверяем по дефолту. состояние как видит страницу
   #assert not btn.said_bar_textbox.visible()
    assert btn.btn_sidebar_first_checkbox.visible()
    assert btn.btn_sidebar_first_checkbox2.visible()
    btn.said_bar.click()
    time.sleep(2)
   # assert not btn.btn_sidebar_first_checkbox2.visible()



time.sleep(3)
