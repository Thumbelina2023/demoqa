from pages.base_page import  BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'

        super().__init__(driver, self.base_url)

        # Создание обьектов елементов, которые надо найти и проверить
        self.tx = WebElement(driver,'#app > div > div > div.pattern-backgound.playgound-header > div')
        self.icon = WebElement(driver, '#app > header > a')
        self.said_bar = WebElement(driver, 'div:nth-child(1) > span > div')
        self.said_bar_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btn_sidebar_first_checkbox2 = WebElement(driver, 'div:nth-child(1) > div > ul > #item-2 > span')
        self.btn_elem = WebElement(driver, 'div:nth-child(1) > div >ul > li')
        self.elem_nav = WebElement(driver, 'div > nav')

        #self.footer_tx = WebElement(driver, '#app > footer > span')


