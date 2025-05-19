import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation_valid():
    customer = Customer("John")
    assert customer.name == "John"

def test_customer_creation_name_too_long():
    with pytest.raises(ValueError):
        Customer("ThisNameIsTooLongForValidation")

def test_customer_creation_name_not_string():
    with pytest.raises(TypeError):
        Customer(123)

def test_coffee_creation_valid():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_creation_name_too_short():
    with pytest.raises(ValueError):
        Coffee("Es")

def test_order_creation_valid():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.50)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.50

def test_order_creation_invalid_price():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)

def test_relationships():
    customer1 = Customer("Bob")
    customer2 = Customer("Carol")
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Cappuccino")
    order1 = Order(customer1, coffee1, 3.50)
    order2 = Order(customer1, coffee1, 4.00)
    order3 = Order(customer1, coffee2, 4.50)
    order4 = Order(customer2, coffee2, 5.00)
    assert len(customer1.orders()) == 3
    assert len(customer2.orders()) == 1
    assert len(customer1.coffees()) == 2
    assert len(customer2.coffees()) == 1
    assert coffee1.num_orders() == 2
    assert coffee2.num_orders() == 2
    assert len(coffee1.customers()) == 1
    assert len(coffee2.customers()) == 2
    assert abs(coffee1.average_price() - 3.75) < 0.01
    assert abs(coffee2.average_price() - 4.75) < 0.01

def test_most_aficionado():
    customer1 = Customer("Dave")
    customer2 = Customer("Eve")
    coffee = Coffee("Mocha")
    Order(customer1, coffee, 3.00)
    Order(customer1, coffee, 4.00)
    Order(customer2, coffee, 4.50)
    Order(customer2, coffee, 4.50)
    most_spent = Customer.most_aficionado(coffee)
    assert most_spent == customer2
    no_orders_coffee = Coffee("Turkish")
    no_result = Customer.most_aficionado(no_orders_coffee)
    assert no_result is None
