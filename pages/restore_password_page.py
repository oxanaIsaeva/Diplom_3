import allure
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step('Делаем скролл на странице до секции "Забыли пароль?"')
    def scroll_to(self, driver, locator):
        element = self.find_element_with_wait(locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
