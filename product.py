from typing import Union


# ---------------------
# Create Classes
class Product:
    """
    Generate Product Class
    """

    def __init__(self, name, price):
        """Class constructor

        Args:
            name (str): Product name.
            price (Union[int, str]): Product price.
        """
        self.name = name
        self.price = price

    def discount(self, percentage):
        """Apply discount pergentage in the product price.

        Args:
            percentage (int): Product discount percentage.
        """
        self.price = self.price - (self.price * (percentage/100))
        print(f'O produto {self.name} custa R${self.price}')

    # ---------------------
    # Concept: Getter and Setter can be a filter to validate the class received values.

    # Getter
    @property
    def price(self):
        """Intercept price value when requested.

        Returns:
            Union[int, float]: property price
        """
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        """Intercept price value when setted.

        Args:
            value (Union[int, str]): Price value
        """
        if isinstance(value, str):
            value = float(value.replace('R$', ''))

        self._price = value

    # ---------------------
