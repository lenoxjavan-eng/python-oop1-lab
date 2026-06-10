#!/usr/bin/env python3
"""Book model for the OOP lab.

This module defines a simple `Book` class with a title and a
page count. The `page_count` property validates that values are
integers and prints a friendly message when invalid input is set.
"""

class Book:
    """A minimal representation of a book.

    Attributes:
        title (str): The book's title.
        page_count (int): Number of pages; enforced to be an int.
    """

    def __init__(self, title, page_count):
        # store the title directly
        self.title = title
        # internal storage for the page count uses a protected attribute
        self._page_count = None
        # use the setter to validate the initial value
        self.page_count = page_count

    @property
    def page_count(self):
        """The book's page count.

        Returns the stored integer value or None if not set.
        """
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Set the page count, validating the type.

        If `value` is not an int, print an error message per the lab
        specification and do not change the stored value.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book.

        Prints a short message used by the tests and by learners to
        exercise method calls on objects.
        """
        print("Flipping the page...wow, you read fast!")

