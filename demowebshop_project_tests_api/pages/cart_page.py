import allure
from demowebshop_project_tests_api.utils.helper import api_request


class Cart:

    def add_item(self, url, endpoint, cookie_customer):
        with allure.step("Отправляется запрос к API на добавление продукта в корзину"):
            response = api_request(url, endpoint, "POST", cookies={'Nop.customer': cookie_customer})

        return response

    def add_item_with_options(self, url, endpoint, payload, cookie_customer):
        with allure.step("Отправляется запрос к API на добавление продукта с заданными характеристиками в корзину"):
            response = api_request(url, endpoint, "POST", data=payload, cookies={'Nop.customer': cookie_customer})

        return response

    def get_items_from_cart(self, url, endpoint, cookie_customer):
        with allure.step("Отправляется запрос к API на получение всех продуктов из корзины"):
            response = api_request(url, endpoint, "GET", cookies={'Nop.customer': cookie_customer})

        return response

    def delete_item(self, url, endpoint, cookie_customer):
        payload = {
            'removefromcart': '4362874',
            'updatecart': 'Update shopping cart'
        }

        with allure.step("Отправляется запрос к API на удаление продукта из корзины"):
            response = api_request(
                url,
                endpoint,
                method="POST",
                data=payload,
                cookies={'Nop.customer': cookie_customer}
            )

        return response


cart = Cart()
