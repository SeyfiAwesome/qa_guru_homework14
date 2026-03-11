import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import have
from pages.main_page import MainPage

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Навигация')
@allure.story('Переход по ссылкам меню')
@allure.title('Клик по пункту меню "Портфолио" открывает страницу с проектами')
def test_portfolio_link_navigation():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click on "Портфолио" link in menu'):
        main_page.click_project_link()

    with allure.step('Verify that portfolio page is opened'):
        main_page.check_project_page_is_opened()

