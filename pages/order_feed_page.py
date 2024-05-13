import allure
import requests

from data import Links
from pages.personal_account_page import PersonalAccountPage


class OrderFeedPage(PersonalAccountPage):

    @allure.step('Получение номера персонального заказа')
    def get_order_number(self, locator_pers_account, locator_order_history, locator_last_pers_order,
                         locator_order_number, locator_close_popup):
        self.find_element_with_wait(locator_pers_account)
        self.click_on_element(locator_pers_account)
        self.click_on_element(locator_order_history)
        self.click_on_element(locator_last_pers_order)
        order_number = self.get_text_from_element(locator_order_number)
        order_number_formatted = order_number[1:]
        self.click_on_element(locator_close_popup)

        return order_number_formatted

    @allure.step('Создание заказа')
    def create_order(self, access_token):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72",
                                   "61c0c5a71d1f82001bdaaa70"]}
        requests.post(f'{Links.URL}/api/orders',
                      headers={"Authorization": access_token},
                      data=payload)

    @allure.step('Получение последнего номера заказа')
    def get_last_order_number(self, locator_order_link, locator_last_order_number):
        self.click_on_element(locator_order_link)
        self.find_element_with_wait(locator_last_order_number)
        last_order_number = self.get_text_from_element(locator_last_order_number)

        return last_order_number
