from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_LINK = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Лента Заказов']"
    # Последний заказ
    LAST_ORDER = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][1]"
    # Номер последнего заказа из "Ленты Заказов"
    POPUP_ORDER_DETAILS = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
    # Окно с деталями заказа
    DONE_TEXT = By.XPATH, ".//p[@class='undefined text text_type_main-default mb-15'][text()='Выполнен']"
    # Текст 'Выполнен' на деталях заказа
    LAST_PERSONAL_ORDER = By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][1]"
    # Последний заказ
    PERSONAL_ORDER_NUMBER = By.XPATH, ".//p[@class='text text_type_digits-default mb-10 mt-5']"
    # Номер последнего заказа
    LAST_ORDER_NUMBER = By.XPATH, ".//li[contains(@class, 'text text_type_digits-default mb-2')][1]"
    # Номер последнего заказа из "Ленты Заказов"
    CLOSE_ORDER_DETAILS = By.XPATH, (".//section[2]/div[1]/button[@class='Modal_modal__close_modified__3V5XS Modal_"
                                     "modal__close__TnseK']")  # Кпопка закрытия деталей заказа
    COUNT_OF_ORDERS_TODAY = By.XPATH, ".//div[3]/p[2][@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    # Количество выполненных за сегодня заказов
    ORDERS_IN_PROGRESS = By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]"
    # Заказы в работе
