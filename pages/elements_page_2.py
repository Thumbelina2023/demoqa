from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'

        super().__init__(driver, self.base_url)

        # Создание обьектов елементов, которые надо найти и проверить

        self.footer_tx = WebElement(driver, '#app > footer > span')
        self.text_c = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
