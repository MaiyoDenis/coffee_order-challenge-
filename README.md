# Coffee Shop Domain Model

## Overview

This project models a Coffee Shop domain using object-oriented programming principles in Python. It consists of three main entities:

- **Customer**: Represents a customer who can place many orders.
- **Coffee**: Represents a type of coffee that can be ordered many times.
- **Order**: Represents an order placed by a customer for a specific coffee at a given price.

The relationships are:
- A Customer can place many Orders.
- A Coffee can have many Orders.
- An Order belongs to one Customer and one Coffee.
- Customer and Coffee have a many-to-many relationship through Orders.

## Project Structure

- `customer.py`: Defines the `Customer` class with properties, validation, and methods to manage orders and coffees.
- `coffee.py`: Defines the `Coffee` class with properties, validation, and methods to manage orders and customers.
- `order.py`: Defines the `Order` class with properties, validation, and associations to Customer and Coffee.
- `debug.py`: Contains test functions to validate the functionality of the classes and their relationships.

## Setup and Installation

1. Create a virtual environment and install dependencies using `pipenv`:

   ```bash
   pipenv install
   pipenv shell
   pipenv install pytest
   ```

2. The project does not have external dependencies beyond standard Python libraries and `pytest` for testing.

## Running Tests

You can run the tests in `debug.py` to verify the implementation:

```bash
python3 debug.py
```

The tests cover:

- Creation and validation of Customer, Coffee, and Order instances.
- Relationship methods between customers, coffees, and orders.
- Aggregate methods like average price and number of orders.
- The `most_aficionado` class method in Customer.

## Usage

You can import the classes in your own scripts and create instances as needed. For example:

```python
from customer import Customer
from coffee import Coffee

customer = Customer("Alice")
coffee = Coffee("Latte")
order = customer.create_order(coffee, 4.50)
```

## Code Quality

- Input validation is implemented to ensure data integrity.
- Exceptions are raised for invalid inputs.
- The code follows Python's PEP 8 style guidelines.
- Relationships between objects are managed through methods and properties.

## License

This project is for educational purposes.

## Author

denis.maiyo@student.moringaschool.com
