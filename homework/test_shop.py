"""
Протестируйте классы из модуля homework_7/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()



class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1000) is None
        assert product.quantity == 0


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert pytest.raises(ValueError, lambda: product.buy(1001))


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_product_add_cart(self, cart, product):

        cart.add_product(product)
        assert product in cart.products
        assert cart.products[product] == 1

        cart.add_product(product)
        assert cart.products[product] == 2


    def test_product_clear_cart(self, cart, product):
        cart.add_product(product, 60)
        cart.clear()
        assert not product in cart.products

    def test_product_remove_cart(self, cart, product):

        cart.add_product(product)
        cart.remove_product(product)
        assert not product in cart.products

        cart.add_product(product)
        cart.remove_product(product, 1)
        assert not product in cart.products

        cart.add_product(product)
        cart.remove_product(product, 2)
        assert not product in cart.products

        cart.add_product(product,3)
        cart.remove_product(product, 2)
        assert cart.products[product] == 1

    def test_product_total_cart(self, cart, product):

        cart.add_product(product, 60)
        assert cart.get_total_price() == 6000

    def test_product_buy_cart(self, cart, product):

        cart.add_product(product, 1001)
        assert pytest.raises(ValueError, lambda: cart.buy())

        cart.clear()
        cart.add_product(product, 1000)
        cart.buy()
        assert product.quantity == 0















