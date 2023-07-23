from pages.base_page import  BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        self.section_content = WebElement(driver,'#section1Content > p')
        self.section_heading = WebElement(driver,'#section1Heading')
        self.section_two_content = WebElement(driver,'#section2Content > p:nth-child(1)')
        self.section_two_content_two = WebElement(driver,'#section2Content > p:nth-child(2)')
        self.section_three_content = WebElement(driver,'#section3Content > p')
        super().__init__(driver, self.base_url)

