from pages.check_box import Check_box


def test_check_box(browser):
    check_box = Check_box(browser)

    check_box.visit()
    assert check_box.str.check_count_elements(count=1)
    check_box.btn_plus.click()

    assert check_box.str.check_count_elements(count=17)
    for element in check_box.str.find_elements():
        assert element.is_displayed()

    browser.refresh()
    assert check_box.str.check_count_elements(count=1)