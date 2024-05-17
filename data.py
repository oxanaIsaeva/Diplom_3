import random


class Links:
    URL = 'https://stellarburgers.nomoreparties.site'
    FORGOT_PASSWORD_URL = '/forgot-password'
    PERSONAL_ACCOUNT_URL = "/account/profile"
    ORDER_HISTORY_URL = "/account/order-history"
    LOGIN_URL = "/login"
    FEED_URL = "/feed"


class Data:
    number = random.randint(1111, 9999)
    CREATE_USER = {
        "email": f"OxanaIsaeva{number}@yandex.ru",
        "password": "Test12345",
        "name": f"OxanaIsaeva{number}"
    }

    USER_DATA = {
        "email": "OxanaIsaeva123@yandex.ru",
        "password": "Test12345"
    }

    INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa75"]
    }
