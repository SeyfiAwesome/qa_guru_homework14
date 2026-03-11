import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support.conditions import be
from selenium.webdriver import ActionChains
import time

from pages.main_page import MainPage


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'seyfiawesome')
@allure.feature('Скачать презентацию')
@allure.story('Проверка наличия, работоспособности кнопки')
@allure.title('Проверка отображения, кликабельности кнопки "Скачать презентацию"')

def test_presentation_button():
    main_page = MainPage()
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Check "Скачать презентацию" button is visible'):
        main_page.check_presentation_button_visible()

    with allure.step('Check "Скачать презентацию" button is clickable'):
        main_page.check_presentation_button_clickable()
