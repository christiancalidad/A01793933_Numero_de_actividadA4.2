"""Module to manage Customers
"""


class Customer:
    """Represents a hotel customer and some basic funtionalities
    """
    def __init__(self):
        self.name = None
        self.id_customer = None
        self.gender = None

    def create_customer(self, name, id_customer, gender):
        """Creates a new customer

        Args:
            name (str): customer name
            id_customer (int): customer identification number
            gender (str): customer gender
        """
        try:
            self.name = name
            self.id_customer = id_customer
            self.gender = gender
        except TypeError:
            raise Exception('Missing arguments')

    def delete_customer(self):
        """Eliminate customer
        """
        self.name = None
        self.id_customer = None
        self.gender = None

    def display_customer_info(self):
        """Prints current customer data
        """
        print(f'Customer name: {self.name}')
        print(f'Customer id: {self.id_customer}')
        print(f'Customer gender: {self.gender}')

    def modify_customer_info(self, field_name, new_value):
        """Modifies a given customer field for a new value

        Args:
            field_name (str): name of the field to modify
            new_value (str,int): nee value to assign
        """
        if field_name == 'name':
            self.name = new_value
        elif field_name == 'id_customer':
            self.id_customer = new_value
        elif field_name == 'gender':
            self.gender = new_value
