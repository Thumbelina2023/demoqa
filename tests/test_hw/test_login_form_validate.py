from pages.form_page import FormPage
import time
def test_login_form_validate(browser):
    form_validate = FormPage(browser)
    form_validate.visit()
    assert form_validate.firt_name.get_dom_attribute('placeholder') == 'First Name'
    #if form_validate.firt_name.send_keys(''):
      # return False
    form_validate.firt_name.send_keys('')
    assert form_validate.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_validate.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_validate.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'

    assert form_validate.user_email.get_dom_attribute('class')  == 'was-validated'

