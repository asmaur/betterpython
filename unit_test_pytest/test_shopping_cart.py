from shopping_cart import ShoppingCart
import pytest
from unittest.mock import Mock
from item_database import ItemDatabase


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_add_item_to_cart(cart):
    cart.add("uva")
    assert cart.size() == 1


def test_cart_contains_item(cart):
    cart.add("Pera")
    assert "Pera" in cart.get_all_item()


def test_cart_contains_item_fail(cart):
    cart.add("Pera")
    assert "Uva" not in cart.get_all_item()


def test_cart_is_full(cart):
    for _ in range(5):
        cart.add("Uva")
    with pytest.raises(OverflowError):
        cart.add("Pera")


def test_get_cart_total_price(cart):
    cart.add("maça")
    cart.add("uva")
    cart.add("pera")
    itemDB = ItemDatabase()

    def mock_get_item(item: str):
        if item == "maça":
            return 5.0
        elif item == "uva":
            return 7.0
        else:
            return 3.0

    itemDB.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(itemDB) == 15.0
