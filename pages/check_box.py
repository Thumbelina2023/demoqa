from pages.base_page import  BasePage
from components.components import WebElement

class Check_box(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        self.str = WebElement(driver, 'span.rct-text')
        self.btn_plus = WebElement(driver, '#tree-node > div > button.rct-option.rct-option-expand-all')

        super().__init__(driver, self.base_url)