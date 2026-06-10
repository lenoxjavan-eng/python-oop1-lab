#!/usr/bin/env python3
"""Coffee model for the OOP lab.

Defines a `Coffee` class with basic validation for `size` and a
`tip()` method which prints a message and increases the price by 1.
"""

class Coffee:
    """A minimal representation of a coffee order.

    Attributes:
        size (str): One of 'Small', 'Medium', or 'Large'.
        price (float): Price in dollars; numeric and mutable.
    """

    def __init__(self, size, price):
        # internal storage for size; setter enforces allowed values
        self._size = None
        # set via property to validate the provided value
        self.size = size
        # price is stored directly; tests expect numeric addition
        self.price = price

    @property
    def size(self):
        """The coffee size (Small, Medium, or Large)."""
        return self._size

    @size.setter
    def size(self, value):
        """Validate the coffee size and print a message on invalid input.

        The setter will not change the stored value if the input is
        invalid, matching the lab's expected behavior.
        """
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """Simulate tipping the barista.

        Prints a friendly acknowledgment and increases the coffee's
        `price` by 1 dollar.
        """
        print("This coffee is great, here’s a tip!")
        self.price += 1