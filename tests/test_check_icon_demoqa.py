#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
from pages.demoqa import DemoQa
import time


def test_check_icon(browser):
    demoqa_page = DemoQa(browser) # присваеваем обьекту класс. browser всегда прописывается только в тестах, а в остальных driver
    demoqa_page.visit() # входит на страницу
    demoqa_page.icon.click() # страница - элемент -метод. так будет всегда обращение

    assert  demoqa_page.equal_url()
    assert demoqa_page.icon.exist() # вызывает проверку элемента




    #browser.get('https://demoqa.com/')
    #try:
     #   browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #except NoSuchElementException:
    #    assert False
    #assert True
    time.sleep(3)