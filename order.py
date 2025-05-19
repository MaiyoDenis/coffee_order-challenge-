class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        """
        Initialize an Order with a customer, coffee, and price.
        
        Args:
            customer (Customer): Customer placing the order
            coffee (Coffee): Coffee being ordered
            price (float): Price of the order (1.0-10.0)
            
        Raises:
            TypeError: If customer or coffee are not the correct types
            ValueError: If price is not between 1.0 and 10.0
        """
        from customer import Customer
        from coffee import Coffee
        
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a valid Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a valid Coffee instance")
        
        try:
            price_float = float(price)
            if not (1.0 <= price_float <= 10.0):
                raise ValueError("Price must be between 1.0 and 10.0")
        except (TypeError, ValueError):
            raise ValueError("Price must be a number between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price_float
        Order.all.append(self)
        
    @property
    def customer(self):
        """Get the customer who placed this order."""
        return self._customer
        
    @customer.setter
    def customer(self, value):
        """
        Set the customer for this order.
        
        Args:
            value (Customer): New customer
            
        Raises:
            TypeError: If not a valid Customer instance
        """
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a valid Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        """Get the coffee for this order."""
        return self._coffee
        
    @coffee.setter
    def coffee(self, value):
        """
        Set the coffee for this order.
        
        Args:
            value (Coffee): New coffee
            
        Raises:
            TypeError: If not a valid Coffee instance
        """
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a valid Coffee instance")
        self._coffee = value
    
    @property
    def price(self):
        """Get the price of this order."""
        return self._price
        
    @price.setter
    def price(self, value):
        """
        Set the price for this order.
        
        Args:
            value (float): New price (1.0-10.0)
            
        Raises:
            ValueError: If price is not between 1.0 and 10.0
        """
        try:
            price_float = float(value)
            if not (1.0 <= price_float <= 10.0):
                raise ValueError("Price must be between 1.0 and 10.0")
        except (TypeError, ValueError):
            raise ValueError("Price must be a number between 1.0 and 10.0")
        self._price = price_float