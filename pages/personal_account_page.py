import allure

from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Логинимся под юзером')
    def login_to_personal_account(self, locator_button, locator_email, text1, locator_password, text2, locator_go):
        self.click_on_element(locator_button)
        self.set_text_to_element(locator_email, text1)
        self.set_text_to_element(locator_password, text2)
        self.click_on_element(locator_go)
