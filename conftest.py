import pytest
import requests

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from data import Data, Links
from locators.personal_account_page_locators import PersonalAccountLocators
from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(Links.URL)
    elif request.param == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(Links.URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    payload = Data.CREATE_USER
    response = requests.post(f'{Links.URL}/api/auth/register', data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(f'{Links.URL}/api/auth/user', headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
    create_user_data = create_new_user[0]
    page = PersonalAccountPage(driver)
    page.login_to_personal_account(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON,
                                   PersonalAccountLocators.EMAIL_FIELD, create_user_data["email"],
                                   PersonalAccountLocators.PASSWORD_FIELD, create_user_data["password"],
                                   PersonalAccountLocators.GO_BUTTON)


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(f'{Links.URL}/api/orders', headers=headers,
                             data=Data.INGREDIENTS)
    return response.json()["order"]["number"]
