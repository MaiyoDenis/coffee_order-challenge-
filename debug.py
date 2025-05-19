#!/usr/bin/env python3
# debug.py - Test file for the Coffee Shop domain

from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    print("=== Testing Customer Creation ===")
    try:
        # Valid customer
        customer = Customer("John")
        print(f"Created customer: {customer.name}")
        
        # Invalid name (too long)
        try:
            Customer("ThisNameIsTooLongForValidation")
            print("Error: Should have raised an exception for too long name")
        except ValueError as e:
            print(f"Correctly caught exception: {e}")
            
        # Invalid name (not a string)
        try:
            Customer(123)
            print("Error: Should have raised an exception for non-string name")
        except TypeError as e:
            print(f"Correctly caught exception: {e}")
            
    except Exception as e:
        print(f"Unexpected error: {e}")
    print()

def test_coffee_creation():
    print("=== Testing Coffee Creation ===")
    try:
        # Valid coffee
        coffee = Coffee("Espresso")
        print(f"Created coffee: {coffee.name}")
        
        # Invalid name (too short)
        try:
            Coffee("Es")
            print("Error: Should have raised an exception for too short name")
        except ValueError as e:
            print(f"Correctly caught exception: {e}")
            
    except Exception as e:
        print(f"Unexpected error: {e}")
    print()

def test_order_creation():
    print("=== Testing Order Creation ===")
    try:
        # Valid order
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 4.50)
        print(f"Created order: {customer.name} ordered {coffee.name} for ${order.price}")
        
        # Invalid price
        try:
            Order(customer, coffee, 15.0)
            print("Error: Should have raised an exception for price > 10.0")
        except ValueError as e:
            print(f"Correctly caught exception: {e}")
            
    except Exception as e:
        print(f"Unexpected error: {e}")
    print()

def test_relationships():
    print("=== Testing Relationships ===")
    # Create test data
    customer1 = Customer("Bob")
    customer2 = Customer("Carol")
    
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Cappuccino")
    
    # Bob orders Americano twice at different prices
    order1 = Order(customer1, coffee1, 3.50)
    order2 = Order(customer1, coffee1, 4.00)
    
    # Bob orders Cappuccino once
    order3 = Order(customer1, coffee2, 4.50)
    
    # Carol orders Cappuccino once
    order4 = Order(customer2, coffee2, 5.00)
    
    # Test customer's orders
    print(f"{customer1.name}'s orders: {len(customer1.orders())}")
    print(f"{customer2.name}'s orders: {len(customer2.orders())}")
    
    # Test customer's coffees
    print(f"{customer1.name}'s unique coffees: {len(customer1.coffees())}")
    print(f"{customer2.name}'s unique coffees: {len(customer2.coffees())}")
    
    # Test coffee's orders
    print(f"{coffee1.name} orders: {coffee1.num_orders()}")
    print(f"{coffee2.name} orders: {coffee2.num_orders()}")
    
    # Test coffee's customers
    print(f"{coffee1.name} unique customers: {len(coffee1.customers())}")
    print(f"{coffee2.name} unique customers: {len(coffee2.customers())}")
    
    # Test average price
    print(f"{coffee1.name} average price: ${coffee1.average_price():.2f}")
    print(f"{coffee2.name} average price: ${coffee2.average_price():.2f}")
    print()

def test_most_aficionado():
    print("=== Testing Most Aficionado ===")
    # Create test data
    customer1 = Customer("Dave")
    customer2 = Customer("Eve")
    
    coffee = Coffee("Mocha")
    
    # Dave spends $7 total on Mocha (across 2 orders)
    Order(customer1, coffee, 3.00)
    Order(customer1, coffee, 4.00)
    
    # Eve spends $9 total on Mocha (across 2 orders)
    Order(customer2, coffee, 4.50)
    Order(customer2, coffee, 4.50)
    
    # Find who spent most on Mocha
    most_spent = Customer.most_aficionado(coffee)
    print(f"Customer who spent most on {coffee.name}: {most_spent.name}")
    
    # Test with coffee that has no orders
    no_orders_coffee = Coffee("Turkish")
    no_result = Customer.most_aficionado(no_orders_coffee)
    print(f"Customer who spent most on {no_orders_coffee.name}: {no_result}")
    print()

if __name__ == "__main__":
    test_customer_creation()
    test_coffee_creation()
    test_order_creation()
    test_relationships()
    test_most_aficionado()
    
    print("All tests completed!")