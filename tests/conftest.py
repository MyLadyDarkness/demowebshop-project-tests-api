import allure
import pytest

from demowebshop_project_tests_api.utils.helper import api_request


@pytest.fixture(scope='function', autouse=True)
def base_url():
    base_url = 'https://demowebshop.tricentis.com'
    return base_url


@pytest.fixture(scope='function', autouse=False)
def cookie_customer(base_url):
    with allure.step('Получение cookie посетителя'):
        result = api_request(url=base_url, endpoint="", method="GET")
        cookie_customer = result.cookies.get('Nop.customer')

    yield cookie_customer
