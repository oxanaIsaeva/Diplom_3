import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Инициализация браузера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Возвращаем текстовое содержимое элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)

        return element.text

    @allure.step('Возвращаем текстовое содержимое элементов')
    def get_text_from_elements(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Получаем текст элемента')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)
