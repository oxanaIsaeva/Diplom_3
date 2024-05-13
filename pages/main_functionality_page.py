
import allure
from selenium.webdriver import ActionChains

from pages.personal_account_page import PersonalAccountPage
from pages.restore_password_page import RestorePasswordPage


class MainFunctionalityPage(PersonalAccountPage, RestorePasswordPage):

    @allure.step('Перетаскивание ингредиента в конструктор')
    def move_ingredient_to_creator(self, driver, ingredient_locator, creator_locator):
        action = ActionChains(driver)
        ingredient = self.find_element_with_wait(ingredient_locator)
        creator = self.find_element_with_wait(creator_locator)
        action.click_and_hold(ingredient).move_to_element(creator).click(creator).perform()
