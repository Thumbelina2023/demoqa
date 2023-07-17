from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import  BasePage
import time

class DemoQa(BasePage): # метод, котрый принимает find_element с аргументом locator

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)


    def exist_icon(self):

        try:
            self.find_element(locator= '#app > header > a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element(locator='#app > header > a').click()

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False



