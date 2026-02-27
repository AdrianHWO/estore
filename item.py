import csv


class Item:  # Conventionally, class names are Capitalized
    all = []
    pay_rate = 0.8  # The default discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, (
            f"Quantity {quantity} is not greater than or equal to zero!"
        )

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        # Using self.pay_rate allows instance-level overrides
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            for item_data in reader:
                # Clean the keys (remove spaces, lowercase) and handle None values
                clean_data = {k.strip().lower(): v for k, v in item_data.items()}

                name = clean_data.get("name") or "Unknown"
                price = clean_data.get("price") or "0"
                qty = clean_data.get("quantity") or "0"

                cls(name=name, price=float(price), quantity=int(qty))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
        )
