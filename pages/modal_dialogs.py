from pages.base_page import  BasePage
from components.components import WebElement

class modal_dialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_modal_dialog = WebElement(driver,'#item-0')
        self.icon = WebElement(driver, '#app > header > a')