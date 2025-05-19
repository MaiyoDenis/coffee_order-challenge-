class Customer:
    all = []
    
    def __init__(self, name):
        """
        Initialize a Customer with a name.
        
        Args:
            name (str): Customer name (1-15 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is not between 1 and 15 characters
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        
        self._name = name
        Customer.all.append(self)
        
    @property
    def name(self):
        """Get the customer's name."""
        return self._name
        
    @name.setter
    def name(self, value):
        """
        Set the customer's name.
        
        Args:
            value (str): New name (1-15 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is not between 1 and 15 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    
    def orders(self):
        """
        Get all orders placed by this customer.
        
        Returns:
            list: List of Order instances associated with this customer
        """
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        """
        Get all unique coffees ordered by this customer.
        
        Returns:
            list: List of unique Coffee instances ordered by this customer
        """
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        """
        Create a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order (1.0-10.0)
            
        Returns:
            Order: The newly created order
            
        Raises:
            Various exceptions if inputs are invalid (handled by Order class)
        """
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        """
        Find the customer who has spent the most money on a specific coffee.
        
        Args:
            coffee (Coffee): The coffee to check
            
        Returns:
            Customer or None: The customer who spent the most, or None if no orders for the coffee
        """
        from order import Order
        
        if coffee is None:
            raise ValueError("A valid Coffee instance must be provided")
        
        # Filter orders for this coffee
        coffee_orders = [order for order in Order.all if order.coffee == coffee]
        
        if not coffee_orders:
            return None
        
        # Calculate total spending per customer
        spending = {}
        for order in coffee_orders:
            customer = order.customer
            if customer not in spending:
                spending[customer] = 0
            spending[customer] += order.price
        
        # Find customer with maximum spending
        max_customer = None
        max_spending = 0
        
        for customer, total in spending.items():
            if total > max_spending:
                max_spending = total
                max_customer = customer
        
        return max_customer