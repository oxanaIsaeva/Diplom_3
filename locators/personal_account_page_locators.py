from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, (".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Личный "
                                         "Кабинет']")  # Кнопка "Личный кабинет" на главной странице
    EMAIL_FIELD = By.XPATH, ".//input[@class='text input__textfield text_type_main-default'][@name='name']"
    # Поле ввода почты
    PASSWORD_FIELD = By.XPATH, ".//input[@class='text input__textfield text_type_main-default'][@name='Пароль']"
    # Поле ввода пароля
    GO_BUTTON = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_"
                           "size_medium__3zxIa'][text()='Войти']")  # Кнопка "Войти"
    PROFILE_TEXT = By.XPATH, (".//a[@class ='Account_link__2ETsJ text text_type_main-medium text_color_inactive "
                              "Account_link_active__2opc9']")  # Текст "Профиль"
    ORDER_HISTORY_CHAPTER = By.XPATH, (".//a[@class ='Account_link__2ETsJ text text_type_main-medium text_color_"
                                       "inactive']")  # Раздел "История заказов"
    GO_OUT_BUTTON = By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    # Кнопка "Выход"
    LOGIN_TEXT = By.XPATH, ".//h2[text()='Вход']"  # Текст "Вход" на странице логина
