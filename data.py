import random


class Links:
    URL = 'https://stellarburgers.nomoreparties.site'
    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    PERSONAL_ACCOUNT_URL = "https://stellarburgers.nomoreparties.site/account/profile"
    ORDER_HISTORY_URL = "https://stellarburgers.nomoreparties.site/account/order-history"
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
    FEED_URL = "https://stellarburgers.nomoreparties.site/feed"


class Data:
    number = random.randint(1111, 9999)
    CREATE_USER = {
        "email": f"OxanaIsaeva{number}@yandex.ru",
        "password": "Test12345",
        "name": f"OxanaIsaeva{number}"
    }
