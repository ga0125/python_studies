"""
Association methodology from OOP.
"""


class Writer:
    """
    Generate Writer class
    """

    def __init__(self, name: str) -> None:
        """Constructor class

        Args:
            name (str): Writer name
        """
        self.__name = name
        self.__tool = ""

    @property
    def name(self) -> str:
        """Getter to access private arguments

        Returns:
            str: Private writer name
        """
        return self.__name

    @property
    def tool(self) -> str:
        """Getter to access private arguments

        Returns:
            str: Private writer tool
        """
        return self.__tool

    @tool.setter
    def tool(self, tool: str) -> None:
        """Set value of the private arguments

        Args:
            tool (str): Private writer tool with a value
        """
        self.__tool = tool


class Pen:
    """
    Generate Pen Class
    """

    def __init__(self, brand: str) -> None:
        """Constructor class

        Args:
            brand (str): Private brand pen
        """
        self.__brand = brand

    @property
    def brand(self):
        """Getter to access private arguments

        Returns:
            str: Private pen brand
        """
        return self.__brand

    def write(self) -> None:
        """Pen's action 
        """
        print('A caneta está escrevendo...')


class Typewriter:
    """
    Generate Pen Class
    """

    def __init__(self, brand: str) -> None:
        """Constructor class

        Args:
            brand (str): Private brand typewriter
        """
        self.__brand = brand

    @property
    def brand(self) -> str:
        """Getter to access private arguments

        Returns:
            str: Private typewriter brand
        """
        return self.__brand

    def write(self):
        """Typewriter's action 
        """
        print('A máquina está escrevendo...')
