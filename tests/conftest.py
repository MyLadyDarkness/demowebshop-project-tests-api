import allure
import pytest

from utils.helper import api_request

BASE_URL = 'https://demowebshop.tricentis.com'

@pytest.fixture(scope='function', autouse=False)
def cookie_customer():
    with allure.step('Получение cookie посетителя'):
        result = api_request(url=BASE_URL, endpoint="", method="GET")
        cookie_customer = result.cookies.get('Nop.customer')

    yield cookie_customer
