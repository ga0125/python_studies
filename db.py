"""
- public (e.g. -> self.data) 
- _private (e.g. -> self.__data)
- __protected (e.g. -> self.__data)
"""


class DataBase:
    """
    Generate DataBase Class
    """

    def __init__(self):
        """Class constructor
        """
        self.__data = {}

    @property
    def data(self) -> dict:
        """Make an argument visible, but unalterable.

        Returns:
            dict: Protected data dict
        """
        return self.__data

    def add_customers(self, id: int, name: str) -> None:
        """Add customer in data dict.

        Args:
            id (int): Customer ID
            name (str): Customer name
        """
        if not 'customers' in self.__data:
            self.__data['customers'] = {id: name}
        else:
            self.__data['customers'].update({id: name})

    def list_customers(self) -> None:
        """List all customers in data dict 
        """
        for id, name in self.__data['customers'].items():
            print(f'ID: {id} || Name: {name}')

    def delete_customer(self, id: int) -> None:
        """Delete a specific customer from the data dict.

        Args:
            id (int): Customer ID
        """
        del self.__data['customers'][id]
