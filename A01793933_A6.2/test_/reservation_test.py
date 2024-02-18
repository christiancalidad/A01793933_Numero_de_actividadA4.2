"""Tests for reservation class and its methods
"""

import unittest
import io
from contextlib import redirect_stdout
from code_.reservation import Reservation


class ReservationTest(unittest.TestCase):
    '''Unit test class to perform Reservation test cases
    '''

    def setUp(self):
        self.reservation = Reservation()

    def test_create_reservation(self):
        """Test reservation creation
        """

        self.reservation.create_reservation(
            hotel='Hotel Buenavista', customer='Juan',
            room=101, date='2024-03-02')
        self.assertIn('Hotel Buenavista', self.reservation.reservations)
        self.assertEqual(
            self.reservation.reservations['Hotel Buenavista'][0]['customer'],
            'Juan')
        self.assertEqual(
            self.reservation.reservations['Hotel Buenavista'][0]['room'],
            101)
        self.assertEqual(
            self.reservation.reservations['Hotel Buenavista'][0]['date'],
            '2024-03-02')

    def test_display_reservation(self):
        """Test rdisplayng reservation info
        """

        self.reservation.create_reservation(
            hotel='Hotel Buenavista', customer='Juan',
            room=101, date='2024-03-02')
        with io.StringIO() as buf, redirect_stdout(buf):
            self.reservation.display_reservations()
            output = buf.getvalue()
        self.assertEqual(output, "Hotel Buenavista [{'customer': 'Juan'," +
                         " 'room': 101, 'date': '2024-03-02'}]\n")

    def test_cancel_reservation(self):
        """Test canceling reservation
        """

        self.reservation.create_reservation(
            hotel='Hotel Buenavista', customer='Juan',
            room=101, date='2024-03-02')
        self.reservation.create_reservation(
            hotel='Hotel Buenavista', customer='Juan',
            room=101, date='2024-03-05')
        self.reservation.eliminate_reservation(
            hotel='Hotel Buenavista', customer='Juan',
            room=101, date='2024-03-05')

        self.assertEqual(len(self.reservation.reservations), 1)

    def test_missing_argument(self):
        """test raising excepcior for not giving all required arguments
        """

        with self.assertRaises(Exception) as context:
            self.reservation.create_reservation(hotel='Hotel Buenavista',
                                                customer='Juan', room=101)
            self.assertTrue('Missing arguments' in context.exception)


if __name__ == '__main__':
    unittest.main()
