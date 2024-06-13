from qa_guru_22_final_tests_api.utils.assertions import assertions
from qa_guru_22_final_tests_api.pages.cart_page import cart
from schemas.response_add_item import response_add_item


def test_add_cart_one_item(base_url, cookie_customer):
    endpoint = "/addproducttocart/catalog/13/1/1"
    response = cart.add_item(base_url, endpoint, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_response_schema(response, response_add_item)


def test_add_cart_item_twice(base_url, cookie_customer):
    endpoint = "/addproducttocart/catalog/22/1/1"

    response = cart.add_item(base_url, endpoint, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_response_schema(response, response_add_item)

    response = cart.add_item(base_url, endpoint, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_response_schema(response, response_add_item)


def test_add_from_product_page(base_url, cookie_customer):
    endpoint = "/addproducttocart/details/75/1"
    payload = {'product_attribute_75_5_31': '96',
               'product_attribute_75_6_32': '101',
               'product_attribute_75_3_33': '102',
               'addtocart_75.EnteredQuantity': '1'}
    response = cart.add_item_with_options(base_url, endpoint, payload=payload, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
    assertions.assert_response_value(response)
    assertions.assert_response_schema(response, response_add_item)


def test_get_items_from_cart(base_url, cookie_customer):
    endpoint = "/cart"
    endpoint2 = "/addproducttocart/catalog/22/1/1"

    response = cart.add_item(base_url, endpoint2, cookie_customer=cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_value(response)

    response = cart.get_items_from_cart(base_url, endpoint, cookie_customer)
    assertions.assert_response_status(response)
    assertions.assert_response_format(response)


def test_delete_from_cart(base_url, cookie_customer):
    endpoint1 = "/addproducttocart/catalog/22/1/1"
    endpoint2 = "/cart"

    cart.add_item(base_url, endpoint1, cookie_customer=cookie_customer)
    response = cart.delete_item(base_url, endpoint2, cookie_customer=cookie_customer)

    assertions.assert_response_status(response)
    assertions.assert_response_format(response)
