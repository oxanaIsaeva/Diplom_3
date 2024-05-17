from selenium.webdriver.common.by import By


class MainFunctionalityLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"  # Линк на секцию "Конструктор"
    CONSTRUCTOR_TEXT = By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10'][text()='Соберите бургер']"
    # Текст "Соберите бургер"
    CONSTRUCTOR_SECTION = By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"
    # Секция "Конструктор"
    ORDER_FEED_BUTTON = By.XPATH, ".//p[text()='Лента Заказов']"  # Линк на секцию "Лента Заказов"
    ORDER_FEED_TEXT = By.XPATH, ".//h1[@class='text text_type_main-large mt-10 mb-5']"  # Текст "Лента Заказов"
    ORDER_HISTORY_SECTION = By.CLASS_NAME, "OrderFeed_contentBox__3-tWb"
    # Секция история заказов
    FLUORESCENT_BUN = By.XPATH, (".//img[@alt='Флюоресцентная булка R2-D3'][@class='BurgerIngredient_ingredient__image"
                                 "__3e-07 ml-4 mr-4']")  # Картинка "Флюоресцентная булка R2-D3"
    INGREDIENT_DETAILS_TEXT = By.XPATH, (".//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m"
                                         " text text_type_main-large pl-10'][text()='Детали ингредиента']")
    # Текст "Детали ингредиента"
    INGREDIENT_DETAILS_POPUP = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']"
    # Окно деталями ингредиента
    CLOSE_POPUP_BUTTON = By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    # Кнопка зыкрытия модального окна
    CONSTRUCTOR = By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']"
    # Конструктор заказов
    FLUORESCENT_BUN_COUNTER = By.XPATH, ".//p[@class='counter_counter__num__3nue1'][text()='2']"
    # Счетчик Флюоресцентной булки
    SPACE_SAUCE = By.XPATH, (".//img[@alt='Соус фирменный Space Sauce'][@class='BurgerIngredient_ingredient__image"
                             "__3e-07 ml-4 mr-4']")  # Соус фирменный Space Sauce
    BEEF_METEORITE = By.XPATH, (".//img[@alt='Говяжий метеорит (отбивная)'][@class='BurgerIngredient_ingredient__image"
                                "__3e-07 ml-4 mr-4']")  # Говяжий метеорит (отбивная)
    CREATE_ORDER_BUTTON = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                     "button_button_size_large__G21Vg'][text()='Оформить заказ']")
    # Кнопка "Оформить заказ"
    POPUP_WITH_ORDER = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']"
    # Окно с номером заказа
    ORDER_IDENTIFIER_TEXT = By.XPATH, (".//p[@class='undefined text text_type_main-medium mb-15'][text()='идентификатор"
                                       " заказа']")  # Текст "идентификатор заказа"
