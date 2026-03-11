import allure
from allure_commons.types import Severity
from pages.main_page import MainPage
from data.users import test_user

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'seyfi_awesome')
@allure.feature('Заявка')
@allure.story('Отправка заявки с главной')
@allure.title('Успешная отправка заявки через попап')

def test_send_request():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click "Оставить заявку" button in header'):
        main_page.click_request_button()

    with allure.step('Fill contact form in popup'):
        main_page.fill_name(test_user.name)
        main_page.fill_phone(test_user.phone)
        main_page.fill_email(test_user.email)

    with allure.step('Accept privacy policy'):
        main_page.accept_privacy_checkbox()

    with allure.step('Submit form'):
        main_page.submit_form()

    with allure.step('Check success message'):
        main_page.check_success_message()
