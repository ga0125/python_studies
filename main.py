# ---------------------
# Imports
from person import Person
from product import Product
from encapsulation import DataBase

# ---------------------
# Instance Person class
person_one = Person('Ciclano', 25)
person_two = Person.by_birth_year('Fulano', 1996)

# ---------------------
# Talking
person_one.talk('POO')
person_one.stop_talk()

person_two.talk('Python')
person_two.stop_talk()

# ---------------------
# Eating
person_one.eat('Churrasco')
person_one.stop_eat()

person_two.eat('Prato Mil')
person_two.stop_eat()

# ---------------------
# Age and birth year
print(person_one.age)
person_one.get_birth_year()

print(person_two.age)
person_two.get_birth_year()

# ---------------------
# Generate ID
print(person_one.generate_id())
print(person_two.generate_id())

# ---------------------
# ---------------------
# Instance Product class
product_one = Product('Camiseta', 50)
product_two = Product('Caneca', 'R$15')

# ---------------------
# Product discount
product_one.discount(10)
product_two.discount(50)

# ---------------------
# ---------------------
# Instance DataBase class
db = DataBase()

# ---------------------
# Add customers
db.add_customers(1, 'Fulano')
db.add_customers(2, 'Ciclano')
db.add_customers(3, 'Beltrano')

# ---------------------
# Delete customer
db.delete_customer(2)

# ---------------------
# List customers
db.list_customers()

# ---------------------
# Accessing a private argument (DO NOT use it on production env)
print(db._DataBase__data)
