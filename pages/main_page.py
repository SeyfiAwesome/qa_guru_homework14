from future.utils import bytes_to_native_str
from selene.support.shared import browser
from selene import have, command
import allure
from selene.support.conditions import be
import time

from selenium.webdriver import ActionChains


class MainPage():
    def __init__(self):
        pass

    def _pause(self, seconds):
        time.sleep(seconds)

    @allure.step('Open main page')
    def open(self):
        browser.open('https://mwi.me/')
        browser.element('.main_header').should(be.visible)

    @allure.step('Click on the "Оставить заявку" button in header')
    def click_request_button(self):
        browser.element('//a[text()="Оставить заявку"]').click()
        self._pause(0.5)
        browser.element('#modal_call').should(be.visible)

    @allure.step('Fill name field with {user_name}')
    def fill_name(self, user_name):
        browser.element('input[placeholder="Имя"]').type(user_name)
        self._pause(0.3)

    @allure.step('Fill telephone with {user_phone}')
    def fill_phone(self, user_phone):
        browser.element('input[placeholder="Телефон"]').type(user_phone)
        self._pause(0.3)

    @allure.step('Fill email with {user_email}')
    def fill_email(self, user_email):
        browser.element('input[placeholder="E-mail"]').type(user_email)
        self._pause(0.3)

    @allure.step('Accept privacy policy checkbox')
    def accept_privacy_checkbox(self):
        browser.element('label.agree-checkbox input[type="checkbox"]').click()
        self._pause(0.3)

    @allure.step('Submit the request form')
    def submit_form(self):
        browser.element('div.submit input[type="button"]').click()
        self._pause(0.3)

    @allure.step('Check success message')
    def check_success_message(self):
        browser.element('//h2[contains(text(), "Спасибо")]').should(be.visible)
        self._pause(0.3)

    @allure.step('Check "Имя" field is highlighted in red while validation error')
    def check_name_field_validation_error(self):
        browser.element('input[placeholder="Имя"').should(have.css_class('feedback-field-req'))
        self._pause(0.3)

    @allure.step('Check "Телефон" field is highlighted in red while validation error')
    def check_phone_field_validation_error(self):
        browser.element('input[placeholder="Телефон"').should(have.css_class('feedback-field-req'))
        self._pause(0.3)

    @allure.step('Check that "Скачать презентацию" button is visible')
    def check_presentation_button_visible(self):
        button = browser.element('a[href="/upload/Prezent_MWI.ME.pdf')
        button.should(be.visible)

    @allure.step('Check that "Скачать презентацию" button is clickable')
    def check_presentation_button_clickable(self):
        button = browser.element('a[href="/upload/Prezent_MWI.ME.pdf"]')
        button.should(be.clickable)

    @allure.step('Check on "Портфолио" link in menu')
    def click_project_link(self):
        browser.element('a[href="https://mwi.me/portfolio/"]').click()
        self._pause(0.5)

    @allure.step('Check that projetcs page is opened')
    def check_project_page_is_opened(self):
        browser.element('.title_page span').should(have.text('ПРОЕКТЫ'))
