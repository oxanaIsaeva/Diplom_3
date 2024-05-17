
import allure

from data import Links
from locators.personal_account_page_locators import PersonalAccountLocators
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators
from conftest import driver, create_new_user, login, create_order


class TestOrderFeedPage:

    @allure.title('Проверка того, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Находим на странице окно с деталями заказа и текст "Выполнен"')
    def test_popup_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        driver.get(Links.URL+Links.FEED_URL)
        order_feed_page.click_on_element(OrderFeedLocators.LAST_ORDER)
        order_feed_page.find_element_with_wait(OrderFeedLocators.POPUP_ORDER_DETAILS)

        assert (order_feed_page.find_element_with_wait(OrderFeedLocators.POPUP_ORDER_DETAILS) and
                order_feed_page.find_element_with_wait(OrderFeedLocators.DONE_TEXT))

    @allure.title('Проверка того, что заказы пользователя из раздела «История заказов» отображаются на странице '
                  '«Лента заказов»')
    @allure.description('Получаем номер последнего персонального заказа и сверяем его с номером последнего заказа на '
                        'странице «Лента заказов»')
    def test_users_orders(self, driver, create_new_user, login, create_order):
        order_feed_page = OrderFeedPage(driver)
        number = order_feed_page.get_order_number(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON,
                                                  PersonalAccountLocators.ORDER_HISTORY_CHAPTER,
                                                  OrderFeedLocators.LAST_PERSONAL_ORDER,
                                                  OrderFeedLocators.PERSONAL_ORDER_NUMBER,
                                                  OrderFeedLocators.CLOSE_ORDER_DETAILS)
        order_feed_page.click_on_element(OrderFeedLocators.ORDER_FEED_LINK)
        order_feed_page.find_element_with_wait(OrderFeedLocators.LAST_ORDER_NUMBER)

        assert order_feed_page.get_text_from_element(OrderFeedLocators.LAST_ORDER_NUMBER) == number

    @allure.title('Проверка того, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Сохраняем номер последнего заказа на странице «Лента заказов», делаем новый заказ,'
                        'проверяем, что номер последнего заказа на странице «Лента заказов» увеличился на 1')
    def test_orders_counter(self, driver, create_new_user, login):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_element(OrderFeedLocators.ORDER_FEED_LINK)
        number_1 = order_feed_page.get_last_order_number(OrderFeedLocators.ORDER_FEED_LINK,
                                                         OrderFeedLocators.LAST_ORDER_NUMBER)
        token = create_new_user[1].json()["accessToken"]
        order_feed_page.create_order(token)
        number_2 = order_feed_page.get_last_order_number(OrderFeedLocators.ORDER_FEED_LINK,
                                                         OrderFeedLocators.LAST_ORDER_NUMBER)

        assert int(number_2) - int(number_1) == 1

    @allure.title('Проверка того, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Сохраняем номер выполненных за сегодня заказов на странице «Лента заказов», '
                        'делаем новый заказ, проверяем, что номер номер выполненных за сегодня заказов на странице '
                        '«Лента заказов» увеличился на 1')
    def test_orders_counter_today(self, driver, create_new_user, login):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_element(OrderFeedLocators.ORDER_FEED_LINK)
        number_1 = order_feed_page.get_last_order_number(OrderFeedLocators.ORDER_FEED_LINK,
                                                         OrderFeedLocators.COUNT_OF_ORDERS_TODAY)
        token = create_new_user[1].json()["accessToken"]
        order_feed_page.create_order(token)
        number_2 = order_feed_page.get_last_order_number(OrderFeedLocators.ORDER_FEED_LINK,
                                                         OrderFeedLocators.COUNT_OF_ORDERS_TODAY)

        assert int(number_2) - int(number_1) == 1

    @allure.title('Проверка того, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Получаем номер последнего персонального заказа и ищем его среди номеров заказов в работе на '
                        'странице «Лента заказов»')
    def test_orders_in_progress(self, driver, create_new_user, login):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.find_element_with_wait(OrderFeedLocators.ORDER_FEED_LINK)
        order_feed_page.click_on_element(OrderFeedLocators.ORDER_FEED_LINK)
        token = create_new_user[1].json()["accessToken"]
        order = order_feed_page.create_order(token)
        order_list = order_feed_page.get_orders_in_progress(OrderFeedLocators.ORDERS_IN_PROGRESS)

        assert str(order) in order_list
