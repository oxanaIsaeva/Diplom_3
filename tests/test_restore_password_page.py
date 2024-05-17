import allure

from data import Data, Links
from locators.restore_password_page_locators import RestorePasswordLocators
from pages.restore_password_page import RestorePasswordPage
from conftest import driver


class TestRestorePasswordPage:

    @allure.title('Проверка, что при нажатии на кнопку «Восстановить пароль» происходит переход на страницу '
                  'восстановления пароля')
    @allure.description('Сверяем текущий url с ожидаемым (data > Links.FORGOT_PASSWORD_URL)')
    def test_jump_to_restore_password_page(self, driver):
        restore_pass_page = RestorePasswordPage(driver)
        restore_pass_page.click_on_element(RestorePasswordLocators.PERSONAL_ACCOUNT_BUTTON)
        restore_pass_page.scroll_to(driver, RestorePasswordLocators.FORGET_PASSWORD_TEXT)
        restore_pass_page.click_on_element(RestorePasswordLocators.PASSWORD_RECOVERY_LINK)

        assert driver.current_url == Links.URL+Links.FORGOT_PASSWORD_URL

    @allure.title('Проверка, что при вводе почты и клику по кнопке «Восстановить» появляется форма восстановления'
                  ' пароля')
    @allure.description('Появляется текст "Восстановление пароля" и поля для ввода нового пароля и кода из письма')
    def test_click_to_restore_button(self, driver):
        restore_pass_page = RestorePasswordPage(driver)
        driver.get(Links.URL+Links.FORGOT_PASSWORD_URL)
        restore_pass_page.set_text_to_element(RestorePasswordLocators.EMAIL_FIELD, Data.USER_DATA["email"])
        restore_pass_page.click_on_element(RestorePasswordLocators.RECOVER_BUTTON)

        assert (restore_pass_page.find_element_with_wait(RestorePasswordLocators.RECOVER_PASSWORD_TEXT) and
                restore_pass_page.find_element_with_wait(RestorePasswordLocators.PASSWORD_FIELD) and
                restore_pass_page.find_element_with_wait(RestorePasswordLocators.CODE_FIELD))

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Появляется рамка, которая подсвечивает поле RestorePasswordLocators.ACTIVE_FIELD')
    def test_click_to_show_password(self, driver):
        restore_pass_page = RestorePasswordPage(driver)
        driver.get(Links.URL+Links.FORGOT_PASSWORD_URL)
        restore_pass_page.set_text_to_element(RestorePasswordLocators.EMAIL_FIELD, Data.USER_DATA["email"])
        restore_pass_page.click_on_element(RestorePasswordLocators.RECOVER_BUTTON)
        restore_pass_page.find_element_with_wait(RestorePasswordLocators.RECOVER_PASSWORD_TEXT)
        restore_pass_page.set_text_to_element(RestorePasswordLocators.NEW_PASSWORD_FIELD,
                                              Data.USER_DATA["password"])
        restore_pass_page.click_on_element(RestorePasswordLocators.SHOW_PASSWORD_BUTTON)

        assert restore_pass_page.find_element_with_wait(RestorePasswordLocators.ACTIVE_FIELD).is_displayed()


