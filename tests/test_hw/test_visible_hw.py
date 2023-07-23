from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    vis_accor = Accordion(browser)
    vis_accor.visit()
    assert vis_accor.section_content.visible()
    vis_accor.section_heading.click()
    time.sleep(2)
    assert not vis_accor.section_content.visible()

def test_visible_accordion_default(browser):
    vis_accord_def = Accordion(browser)
    vis_accord_def.visit()


    assert not vis_accord_def.section_two_content.visible()
    assert not vis_accord_def.section_two_content_two.visible()
    assert not vis_accord_def.section_three_content.visible()



