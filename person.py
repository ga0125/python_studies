# ---------------------
# Import
from datetime import datetime
from random import randint


# ---------------------
# Create Classes
class Person:
    """
    Generate Person Class
    """
    ACTUAL_YEAR = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name: str, age: int, eating: bool = False, talking: bool = False) -> None:
        """Class constructor 

        Args:
            name (str): Person name.
            age (int): Person age.
            eating (bool, optional): Person action. Defaults to False.
            talking (bool, optional): Person action. Defaults to False.
        """
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def talk(self, subject: str) -> None:
        """Person starts talking.

        Args:
            subject (str): Conversation subject.
        """
        if self.eating:
            print(f'{self.name} não pode falar comendo.')
            return

        if self.talking:
            print(f'{self.name} já está falando.')
            return

        print(f'{self.name} está falando sobre {subject}.')
        self.talking = True

    def stop_talk(self) -> None:
        """Person stops talking.
        """
        if not self.talking:
            print(f'{self.name} não está falando.')
            return

        print(f'{self.name} parou de falar.')
        self.talking = False

    def eat(self, food: str) -> None:
        """Person starts eating.

        Args:
            food (str): Food type.
        """
        if self.eating:
            print(f'{self.name} já está comendo.')
            return

        if self.talking:
            print(f'{self.name} não pode comer falando.')
            return

        print(f'{self.name} está comendo {food}.')
        self.eating = True

    def stop_eat(self) -> None:
        """Person stops eating.
        """
        if not self.eating:
            print(f'{self.name} não está comendo.')
            return

        print(f'{self.name} parou de comer.')
        self.eating = False

    def get_birth_year(self) -> None:
        """Calculate birth year of the Person. 
        """
        birth_year = self.ACTUAL_YEAR - self.age
        print(f'{self.name} nasceu em {birth_year}')

    # ---------------------
    # Concept: is an inbuilt function in Python, which returns a class method for a given function.
    # ---------------------
    @classmethod
    def by_birth_year(cls, name: str, birth_year: int):
        """Instancing Person object with others arguments

        Args:
            name (str): Person name.
            birth_year (int): Person birth year. 

        Returns:
            class: Person object instance.
        """
        age = cls.ACTUAL_YEAR - birth_year
        return cls(name, age)

    # ---------------------
    # Concept: is an built-in function returns a static method for a given function.
    # ---------------------
    @staticmethod
    def generate_id() -> int:
        """Generate Person ID

        Returns:
            int: random number. Range -> (10000, 19999)
        """
        rand = randint(10000, 19999)

        return rand
