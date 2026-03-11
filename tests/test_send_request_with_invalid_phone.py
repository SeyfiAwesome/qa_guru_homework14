import allure
from allure_commons.types import Severity

from data.users import test_user_with_invalid_phone
from pages.main_page import MainPage


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Заявка')
@allure.story('Негативные сценарии')
@allure.title('Отправка заявки с некорректным номером телефона')
def test_send_request_with_invalid_phone():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click "Оставить заявку" button in header'):
        main_page.click_request_button()

    with allure.step('Fill "Name", "Email" fields with valid data and "Phone" field with INVALID data'):
        main_page.fill_name(test_user_with_invalid_phone.name)
        main_page.fill_phone(test_user_with_invalid_phone.phone)
        main_page.fill_email(test_user_with_invalid_phone.email)

    with allure.step('Accept privacy policy'):
        main_page.accept_privacy_checkbox()

    with allure.step('Submit form'):
        main_page.submit_form()

    with allure.step('Check "Phone" field is highlighted in red'):
        main_page.check_phone_field_validation_error()
