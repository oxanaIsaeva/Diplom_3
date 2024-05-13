from selenium.webdriver.common.by import By


class RestorePasswordLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, (".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Личный "
                                         "Кабинет']")  # Кнопка "Личный кабинет" на главной странице
    PASSWORD_RECOVERY_LINK = By.XPATH, ".//a[text()='Восстановить пароль']"
    # Линк "Восстановить пароль", переход к форме восстановления пароля
    FORGET_PASSWORD_TEXT = By.XPATH, (".//p[@class ='undefined text text_type_main-default text_color_inactive' and "
                                      "text()='Забыли пароль?']")  # Текст "Забыли пароль?"
    EMAIL_FIELD = By.XPATH, ".//input[@class ='text input__textfield text_type_main-default']"
    # Поле для ввода почты на форме восстановления пароля
    RECOVER_BUTTON = By.XPATH, (".//button[@class ='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                "button_button_size_medium__3zxIa'][text()='Восстановить']")
    # Кнопка "Восстановить" на форме восстановления пароля
    RECOVER_PASSWORD_TEXT = By.XPATH, ".//h2[text() ='Восстановление пароля']"
    # Текст 'Восстановление пароля' на форме восстановления пароля
    PASSWORD_FIELD = By.XPATH, ".//div[@class ='input pr-6 pl-6 input_type_password input_size_default']"
    # Поле "Пароль" на форме восстановления пароля
    CODE_FIELD = By.XPATH, ".//div[@class ='input pr-6 pl-6 input_type_text input_size_default']"
    # Поле "Введите код из письма" на форме восстановления пароля
    NEW_PASSWORD_FIELD = By.XPATH, ".//input[@class ='text input__textfield text_type_main-default'][@type='password']"
    # Поле "Введите новый пароль" на форме восстановления пароля
    SHOW_PASSWORD_BUTTON = By.XPATH, ".//div[@class ='input__icon input__icon-action']"
    ACTIVE_FIELD = By.XPATH, (".//div[@class ='input pr-6 pl-6 input_type_text input_size_default "
                              "input_status_active']")
    # Поле "Введите новый пароль" активно, подсвечивается
    CLICK = By.XPATH, ".//main[@class ='App_componentContainer__2JC2W']"  # Форма восстановления пароля

