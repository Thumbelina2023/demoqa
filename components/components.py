#Создается для того, чтобы отделить все методы работы с элементом от работы со страницой

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click() # создаем метод клик по элементу

    def exist(self):
        try:
            self.find_element() #поиск элемента
        except NoSuchElementException:
            return False

        return True
    def get_text(self):
        return self.find_element().text