import allure
from jsonschema import validate


class Assertions:

    def assert_response_status(self, response):
        with allure.step(f'Проверка, что получен успешный ответ, status_code = {response.status_code}'):
            assert response.status_code == 200

    def assert_response_value(self, response):
        with allure.step(f'Проверка, что в ответе получено корректное значение'
                         f'\nresponse.json()["success"] = {response.json()['success']}'
                         f'\nresponse.json()["message"] = {response.json()['message']}'
                         f'\nколичество предметов в корзине {response.json()['updatetopcartsectionhtml']}'):
            assert response.json()['success'] is True
            assert response.json()[
                       'message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'

    def assert_response_schema(self, response, schema):
        with allure.step('Проверка схемы ответа'):
            validate(response.json(), schema=schema)

    def assert_response_format(self, response):
        with allure.step('Проверка формата ответа'):
            assert 'text/html' in response.headers['Content-Type'].lower()


assertions = Assertions()
