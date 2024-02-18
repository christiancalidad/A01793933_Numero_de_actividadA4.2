"""Module to manage reservations
"""


class Reservation:
    """ Represents a reservations directory and some basic funtionalities
    """

    def __init__(self):
        self.reservations = {}

    def create_reservation(self, hotel, customer, room, date):
        """Creates a new reservation for the given hotel

        Args:
            hotel (str): Hotel's name
            customer (str): Customer's name
            room (int): Room's number
            date (str): Reservation date
        """
        try:
            if hotel not in self.reservations:
                self.reservations.update({hotel: [{'customer': customer,
                                                'room': room, 'date': date}]})
            else:
                self.reservations[hotel].append({'customer': customer,
                                                'room': room, 'date': date})
        except TypeError:
            raise Exception('Missing arguments')

    def display_reservations(self):
        """Print all the current reservations
        """
        for k, v in self.reservations.items():
            print(k, v)

    def eliminate_reservation(self, hotel, customer, room, date):
        """Eliminate a reservation that match to the given data

        Args:
            hotel (str): Hotel's name
            customer (str): Customer's name
            room (int): Room's number
            date (str): Reservation date
        """

        for k, _ in self.reservations.items():
            if k == hotel:
                for i in range(len(self.reservations[hotel])):
                    reservation = self.reservations[hotel][i]
                    if reservation['customer'] == customer and\
                        reservation['room'] == room and \
                            reservation['date'] == date:
                        self.reservations[hotel].pop(i)
