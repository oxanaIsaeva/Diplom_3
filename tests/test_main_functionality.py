import allure

from data import Links
from pages.main_functionality_page import MainFunctionalityPage
from locators.main_functionality_locators import MainFunctionalityLocators
from conftest import driver, create_new_user, login


class TestMainFunctionalityPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Находим на странице текст "Соберите бургер" и конструктор')
    def test_go_to_constructor(self, driver):
        main_func_page = MainFunctionalityPage(driver)
        driver.get(Links.URL+Links.LOGIN_URL)
        main_func_page.click_on_element(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_TEXT)

        assert (main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_TEXT) and
                main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_SECTION))

    @allure.title('Проверка перехода по клику на на «Лента заказов»')
    @allure.description('Находим на странице текст "Лента заказов" и секцию история заказов')
    def test_go_order_feed(self, driver):
        main_func_page = MainFunctionalityPage(driver)
        main_func_page.click_on_element(MainFunctionalityLocators.ORDER_FEED_BUTTON)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.ORDER_FEED_TEXT)

        assert (main_func_page.find_element_with_wait(MainFunctionalityLocators.ORDER_FEED_TEXT) and
                main_func_page.find_element_with_wait(MainFunctionalityLocators.ORDER_HISTORY_SECTION))

    @allure.title('Проверка того, что при клике на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Находим на странице текст "Детали ингредиента" и окно с деталями')
    def test_open_ingredient_details(self, driver):
        main_func_page = MainFunctionalityPage(driver)
        main_func_page.click_on_element(MainFunctionalityLocators.FLUORESCENT_BUN)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_DETAILS_TEXT)

        assert (main_func_page.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_DETAILS_TEXT) and
                main_func_page.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_DETAILS_POPUP))

    @allure.title('Проверка того, что всплывающее окно закрывается кликом по крестику')
    @allure.description('Находим на странице текст "Соберите бургер" и конструктор')
    def test_close_popup(self, driver):
        main_func_page = MainFunctionalityPage(driver)
        main_func_page.click_on_element(MainFunctionalityLocators.FLUORESCENT_BUN)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.INGREDIENT_DETAILS_TEXT)
        main_func_page.click_on_element(MainFunctionalityLocators.CLOSE_POPUP_BUTTON)

        assert (main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_TEXT) and
                main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_SECTION))

    @allure.title('Проверка того, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Элемент счетчик Флюоресцентной булки (MainFunctionalityLocators.FLUORESCENT_BUN_COUNTER) '
                        'с текстом "2" присутствует на странице')
    def test_ingredient_counter(self, driver):
        main_func_page = MainFunctionalityPage(driver)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_TEXT)
        main_func_page.move_ingredient_to_creator(driver, MainFunctionalityLocators.FLUORESCENT_BUN,
                                                  MainFunctionalityLocators.CONSTRUCTOR)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.FLUORESCENT_BUN_COUNTER)

        assert main_func_page.find_element_with_wait(MainFunctionalityLocators.FLUORESCENT_BUN_COUNTER)

    @allure.title('Проверка того, что залогиненный пользователь может оформить заказ')
    @allure.description('Окно с номером заказа и текст "идентификатор заказа" присутствуют на экране')
    def test_create_order(self, driver, create_new_user, login):
        main_func_page = MainFunctionalityPage(driver)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.CONSTRUCTOR_TEXT)
        main_func_page.create_order_gui(driver, MainFunctionalityLocators.FLUORESCENT_BUN,
                                    MainFunctionalityLocators.CONSTRUCTOR,
                                    MainFunctionalityLocators.SPACE_SAUCE,
                                    MainFunctionalityLocators.BEEF_METEORITE,
                                    MainFunctionalityLocators.CREATE_ORDER_BUTTON)
        main_func_page.find_element_with_wait(MainFunctionalityLocators.ORDER_IDENTIFIER_TEXT)

        assert (main_func_page.find_element_with_wait(MainFunctionalityLocators.ORDER_IDENTIFIER_TEXT) and
                main_func_page.find_element_with_wait(MainFunctionalityLocators.POPUP_WITH_ORDER))
