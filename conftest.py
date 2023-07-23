# всегда согдаем этот файл, если есть в тесте хоть один класс!
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')   #def test(browes) так записывать функцию, чтобы можно было ее использовать в других файлах
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width = 1000, height = 1000)
    yield driver
    driver.quit()

