"""Tests for customer class and its methods
"""
import unittest
import io
from contextlib import redirect_stdout
from code_.customer import Customer


class CustomerTest(unittest.TestCase):
    '''Unit test class to perform Customer test cases
    '''

    def setUp(self):
        self.customer = Customer()

    def test_create_customer(self):
        """Test customer creation
        """
        self.customer.create_customer(name='Juan',
                                      id_customer=10566474, gender='Masculino')
        self.assertEqual(self.customer.name, 'Juan')
        self.assertEqual(self.customer.id_customer, 10566474)
        self.assertEqual(self.customer.gender, 'Masculino')

    def test_display_customer(self):
        """Test displaying customer information
        """
        self.customer.create_customer(name='Juan',
                                      id_customer=10566474, gender='Masculino')
        with io.StringIO() as buf, redirect_stdout(buf):
            self.customer.display_customer_info()
            output = buf.getvalue()
        self.assertEqual(output, 'Customer name: Juan\nCustomer id: 10566474' +
                         '\nCustomer gender: Masculino\n')

    def test_modify_customer(self):
        """Test modifyng customer data
        """
        self.customer.create_customer(name='Juan',
                                      id_customer=10566474, gender='Masculino')
        self.customer.modify_customer_info('name', 'Carlos')
        self.customer.modify_customer_info('id_customer', 105664745)
        self.assertEqual(self.customer.name, 'Carlos')
        self.assertEqual(self.customer.id_customer, 105664745)

    def test_delete_customer(self):
        """_test customer deleting
        """
        self.customer.create_customer(name='Juan',
                                      id_customer=10566474, gender='Masculino')
        self.customer.delete_customer()
        self.assertIsNone(self.customer.name)
        self.assertIsNone(self.customer.id_customer)
        self.assertIsNone(self.customer.gender)

    def test_missing_argument(self):
        """test raising excepcior for not giving all required arguments
        """
        with self.assertRaises(Exception) as context:
            self.customer.create_customer(name='Juan', id_customer=10566474)
            self.assertTrue('Missing arguments' in context.exception)


if __name__ == '__main__':
    unittest.main()
