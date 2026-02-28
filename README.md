# estore
Project Structure
main.py: The entry point that orchestrates the application logic.

item.py: The Base Class defining core attributes like name, price, and quantity.

phone.py: A Subclass that inherits from Item, adding specific features like "broken phones" or "N-SIM support."

items.csv: The database layer where all product information is stored and retrieved.

Key OOP Concepts Applied
This project isn't just a script; it’s a demonstration of professional coding patterns:

Inheritance: The Phone class inherits all functionality from Item but adds its own unique logic, reducing code duplication.

Class Methods (@classmethod): Used in item.py to instantiate objects directly from the items.csv file.

Static Methods (@staticmethod): Used for utility logic, such as validating if a price is an integer.

Encapsulation: Protecting attributes to ensure data integrity (e.g., ensuring quantity cannot be negative).

Magic Methods (__repr__): Overridden to provide a readable and professional representation of objects for debugging.
