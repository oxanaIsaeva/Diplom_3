import allure
import requests

from data import Links, Data
from pages.personal_account_page import PersonalAccountPage
from locators.personal_account_page_locators import PersonalAccountLocators
from conftest import driver


class TestPersonalAccountPage:
    accessToken = ""
    email = ""
    password = "Test12345"

    @classmethod
    def setup_class(cls):
        payload = Data.CREATE_USER
        response = requests.post(f'{Links.URL}/api/auth/register', data=payload)
        format_response = response.json()
        TestPersonalAccountPage.accessToken = format_response["accessToken"]
        user_information = format_response['user']
        TestPersonalAccountPage.email = user_information['email']

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Сверяем текущий url с ожидаемым (data > Links.PERSONAL_ACCOUNT_URL), находим текст "Профиль"')
    def test_jump_to_restore_password_page(self, driver):
        personal_acc_page = PersonalAccountPage(driver)
        driver.get(Links.URL)
        personal_acc_page.login_to_personal_account(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON,
                                       PersonalAccountLocators.EMAIL_FIELD, TestPersonalAccountPage.email,
                                       PersonalAccountLocators.PASSWORD_FIELD, TestPersonalAccountPage.password,
                                       PersonalAccountLocators.GO_BUTTON)
        personal_acc_page.find_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.click_on_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.find_element_with_wait(PersonalAccountLocators.PROFILE_TEXT)

        assert (driver.current_url == Links.PERSONAL_ACCOUNT_URL and
                personal_acc_page.find_element_with_wait(PersonalAccountLocators.PROFILE_TEXT))

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('Сверяем текущий url с ожидаемым (data > Links.ORDER_HISTORY_URL)')
    def test_go_to_order_history(self, driver):
        personal_acc_page = PersonalAccountPage(driver)
        driver.get(Links.URL)
        personal_acc_page.login_to_personal_account(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON,
                                       PersonalAccountLocators.EMAIL_FIELD, TestPersonalAccountPage.email,
                                       PersonalAccountLocators.PASSWORD_FIELD, TestPersonalAccountPage.password,
                                       PersonalAccountLocators.GO_BUTTON)
        personal_acc_page.find_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.click_on_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.click_on_element(PersonalAccountLocators.ORDER_HISTORY_CHAPTER)

        assert driver.current_url == Links.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Сверяем текущий url с ожидаемым (data > Links.LOGIN_URL)')
    def test_log_out_from_account(self, driver):
        personal_acc_page = PersonalAccountPage(driver)
        driver.get(Links.URL)
        personal_acc_page.login_to_personal_account(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON,
                                       PersonalAccountLocators.EMAIL_FIELD, TestPersonalAccountPage.email,
                                       PersonalAccountLocators.PASSWORD_FIELD, TestPersonalAccountPage.password,
                                       PersonalAccountLocators.GO_BUTTON)
        personal_acc_page.find_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.click_on_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_acc_page.click_on_element(PersonalAccountLocators.GO_OUT_BUTTON)
        personal_acc_page.find_element_with_wait(PersonalAccountLocators.LOGIN_TEXT)

        assert driver.current_url == Links.LOGIN_URL

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Links.URL}/api/auth/user',
                        headers={"Authorization": TestPersonalAccountPage.accessToken})
