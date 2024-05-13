from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_LINK = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Лента Заказов']"
    # Линка на секцию "Лента Заказов"
    LAST_ORDER = By.XPATH, "//*[@id='root']/div/main/div/div/ul/li[1]/a"  # Последний заказ
    POPUP_ORDER_DETAILS = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
    # Окно с деталями заказа
    DONE_TEXT = By.XPATH, ".//p[@class='undefined text text_type_main-default mb-15'][text()='Выполнен']"
    # Текст 'Выполнен' на деталях заказа
    LAST_PERSONAL_ORDER = By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[1]"  # Последний заказ
    PERSONAL_ORDER_NUMBER = By.XPATH, ".//p[@class='text text_type_digits-default mb-10 mt-5']"
    # Номер последнего заказа
    LAST_ORDER_NUMBER = By.XPATH, "//*[@id='root']/div/main/div/div/div/div[1]/ul[1]/li[1]"
    # Номер последнего заказа из "Ленты Заказов"
    CLOSE_ORDER_DETAILS = By.XPATH, "//*[@id='root']/div/section[2]/div[1]/button"
    # Кпопка закрытия деталей заказа
    COUNT_OF_ORDERS_TODAY = By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[2]"
    # Количество выполненных за сегодня заказов
    ORDERS_IN_PROGRESS = By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]"
    # Заказы в работе
