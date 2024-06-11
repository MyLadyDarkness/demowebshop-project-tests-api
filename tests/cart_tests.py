from api.assertions import assertions
from api.cart_page import cart

from schemas.response_add_item import response_add_item
from tests.conftest import BASE_URL


def test_add_cart_one_item(cookie_customer):
    endpoint = "/addproducttocart/catalog/13/1/1"
    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_schema(response, response_add_item)


def test_add_cart_item_twice(cookie_customer):
    endpoint = "/addproducttocart/catalog/22/1/1"

    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_schema(response, response_add_item)

    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_schema(response, response_add_item)


def test_add_from_product_page(cookie_customer):
    endpoint = "/addproducttocart/details/75/1"
    payload = {'product_attribute_75_5_31': '96',
               'product_attribute_75_6_32': '101',
               'product_attribute_75_3_33': '102',
               'addtocart_75.EnteredQuantity': '1'}
    response = cart.add_item_with_options(BASE_URL, endpoint, payload=payload, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_schema(response, response_add_item)


def test_get_items_from_cart(cookie_customer):
    endpoint = "/cart"
    endpoint2 = "/addproducttocart/catalog/22/1/1"

    response = cart.add_item(BASE_URL, endpoint2, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)

    response = cart.get_items_from_cart(BASE_URL, endpoint, cookie_customer)
    assertions.assert_response_status(response)


def test_delete_from_cart(cookie_customer):
    endpoint1 = "/addproducttocart/catalog/22/1/1"
    endpoint2 = "/cart"

    cart.add_item(BASE_URL, endpoint1, cookie_customer=cookie_customer)
    response = cart.delete_item(BASE_URL, endpoint2, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
