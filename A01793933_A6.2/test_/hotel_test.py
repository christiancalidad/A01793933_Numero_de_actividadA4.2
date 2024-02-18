"""Tests for hotel class and its methods
"""

import unittest
import io
from contextlib import redirect_stdout
from code_.hotel import Hotel


class HotelTest(unittest.TestCase):
    '''Unit test class to perform hotel test cases
    '''

    def setUp(self):
        self.hotel = Hotel()

    def test_create_hotel(self):
        """Test hotel creation
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        self.assertEqual(self.hotel.name, 'Hotel Buenavista')
        self.assertEqual(self.hotel.adress, 'Calle 65')
        self.assertEqual(self.hotel.rooms,
                         [100, 101, 102, 103, 104, 201, 202, 203, 204, 205])

    def test_display_hotel(self):
        """Test displaying gotel information
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        with io.StringIO() as buf, redirect_stdout(buf):
            self.hotel.display_hotel_info()
            output = buf.getvalue()
        self.assertEqual(
            output,
            'Hotel name: Hotel Buenavista\n' +
            'Hotel adress: Calle 65\n' +
            'Hotel rooms: [100, 101, 102, 103, 104, 201' +
            ', 202, 203, 204, 205]\n' +
            'Hotel reservations: {}\n' +
            'Hotel avaliable rooms: 10\n' + 'Hotel bussy rooms: 0\n')
        
    def test_delete_hotel(self):
        """_test customer deleting
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        self.hotel.delete_hotel()
        self.assertIsNone(self.hotel.name)
        self.assertIsNone(self.hotel.adress)
        self.assertEqual(self.hotel.rooms,[])

    def test_modify_hotel(self):
        """Test modifyng hotel data
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        self.hotel.modify_hotel_info('name', 'Hotel Malavista')
        self.hotel.modify_hotel_info('adress', 'Calle 10')
        self.assertEqual(self.hotel.name, 'Hotel Malavista')
        self.assertEqual(self.hotel.adress, 'Calle 10')

    def test_reserve_room_hotel(self):
        """Test reserving room
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        self.hotel.reserve_room(
            room_number=101, date='2024-05-05', customer='Jhon')
        self.assertEqual(self.hotel.reservations,
                         {101: {'date': '2024-05-05', 'customer': 'Jhon'}})

    def test_cancel_reserve_room_hotel(self):
        """Test cancel reserve
        """
        self.hotel.create_hotel(
            name='Hotel Buenavista', adress='Calle 65',
            rooms=[100, 101, 102, 103, 104, 201, 202, 203, 204, 205])
        self.hotel.reserve_room(
            room_number=101, date='2024-05-05', customer='Jhon')
        self.hotel.cancel_reservation(101)
        self.assertEqual(self.hotel.reservations, {})

    def test_missing_argument(self):
        """test raising excepcior for not giving all required arguments
        """
        with self.assertRaises(Exception) as context:
            self.hotel.create_hotel(name='Hotel Buenavista', adress='Calle 65')
            self.assertTrue('Missing arguments' in context.exception)


if __name__ == '__main__':
    unittest.main()
