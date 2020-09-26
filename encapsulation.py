"""
public, protected, private 
"""


class DataBase:
    def __init__(self):
        self.data = {}

    def add_customers(self, id, name):
        if not 'customers' in self.data:
            self.data['customers'] = {id: name}
        else:
            self.data['customers'].update({id: name})

    def list_customers(self):
        for id, name in self.data['customers'].items():
            print(f'ID: {id} || Name: {name}')

    def delete_customer(self, id):
        del self.data['customers'][id]
