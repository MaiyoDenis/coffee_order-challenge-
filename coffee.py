class Coffee:
    all = []
    
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        
        Args:
            name (str): Coffee name (at least 3 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name is less than 3 characters
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        self._name = name
        Coffee.all.append(self)
        
    @property
    def name(self):
        """Get the coffee's name."""
        return self._name
        
    @name.setter
    def name(self, value):
        """
        Set the coffee's name.
        
        Args:
            value (str): New name (at least 3 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name is less than 3 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value
    
    def orders(self):
        """
        Get all orders for this coffee.
        
        Returns:
            list: List of Order instances for this coffee
        """
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        """
        Get all unique customers who have ordered this coffee.
        
        Returns:
            list: List of unique Customer instances who ordered this coffee
        """
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        """
        Get the total number of times this coffee has been ordered.
        
        Returns:
            int: Number of orders for this coffee
        """
        return len(self.orders())
    
    def average_price(self):
        """
        Calculate the average price of this coffee based on its orders.
        
        Returns:
            float: Average price, or 0 if no orders
        """
        orders = self.orders()
        if not orders:
            return 0
        
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)