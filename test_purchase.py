"""Тесты покупки товара (Части 2 и 3)."""
from purchase import buy_product, SUCCESS_TEXT


def test_purchase_item(browser, url):
    """Покупка товара заканчивается сообщением об успешном заказе."""
    result = buy_product(browser, url)
    assert result == SUCCESS_TEXT
