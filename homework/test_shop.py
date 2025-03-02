"""
Протестируйте классы из модуля homework_7/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
        book1 = Product("book", 100, "This is a book", 1000)
        book2 = Product("Book1", 110, "Cool Book", 500)
        return [book1, book2]

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
        assert product[0].check_quantity(1000)
        assert not product[0].check_quantity(1001)
        assert product[1].check_quantity(500)
        assert not product[1].check_quantity(501)


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product[0].buy(1000)
        product[1].buy(1)
        assert product[0].quantity == 0
        assert product[1].quantity == 499



    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert pytest.raises(ValueError, lambda: product[0].buy(1001))


class TestCart:

    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_product_add_cart(self, cart, product):

        cart.add_product(product[0])
        assert product[0] in cart.products
        assert cart.products[product[0]] == 1

        cart.add_product(product[0])
        assert cart.products[product[0]] == 2

        cart.add_product(product[1], 500)
        assert product[1] in cart.products
        assert cart.products[product[1]] == 500




    def test_product_clear_cart(self, cart, product):
        cart.add_product(product[0], 60)
        cart.clear()
        assert not product[0] in cart.products

    def test_product_remove_cart(self, cart, product):

        cart.add_product(product[0], 5)
        cart.remove_product(product[0])
        assert not product[0] in cart.products

        cart.add_product(product[1],5)
        cart.remove_product(product[1], 6)
        assert not product[1] in cart.products

    def test_product_total_cart(self, cart, product):

        cart.add_product(product[0], 60)
        cart.add_product(product[1], 2)
        assert cart.get_total_price() == 6220

    def test_product_buy_cart(self, cart, product):

        cart.add_product(product[0], 1001)
        assert pytest.raises(ValueError, lambda: cart.buy())














