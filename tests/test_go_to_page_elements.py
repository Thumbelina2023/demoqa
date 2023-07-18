from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    d_q =  DemoQa(browser)
    elem = ElementsPage(browser)

    d_q.visit()
    assert d_q.equal_url()

    d_q.icon.click() # страница - элемент -метод. так будет всегда обращение

    d_q.btn_elements.click() # страница - элемент -метод. так будет всегда обращение

    assert  elem.equal_url() #проверка урла

