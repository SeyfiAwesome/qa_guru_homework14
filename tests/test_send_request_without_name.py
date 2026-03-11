import allure
from allure_commons.types import Severity
from pages.main_page import MainPage
from data.users import test_user, test_user_with_invalid_name


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Заявка')
@allure.story('Негативные сценарии')
@allure.title('Отправка заявки c пустым значением поля "ИМЯ" ')
def test_send_request_without_name():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click "Оставить заявку" button in header'):
        main_page.click_request_button()

    with allure.step('Fill INVALID NAME in name field'):
        main_page.fill_name(test_user_with_invalid_name.name)

    with allure.step('Fill other fields with valid data'):
        main_page.fill_phone(test_user_with_invalid_name.phone)
        main_page.fill_email(test_user_with_invalid_name.email)

    with allure.step('Accept privacy policy'):
        main_page.accept_privacy_checkbox()

    with allure.step('Submit form'):
        main_page.submit_form()

    with allure.step('Check that name field is highlighted in red'):
        main_page.check_name_field_validation_error()
