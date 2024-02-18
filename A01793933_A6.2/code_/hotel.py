"""Module to manage hotels
"""


class Hotel:
    """Representes a hotel and some basic funtionalities
    """
    def __init__(self):
        self.name = None
        self.adress = None
        self.rooms = []
        self.reservations = {}
        self.avaliable_rooms = 0
        self.bussy_rooms = 0

    def create_hotel(self, name, adress, rooms):
        """creates a hotel from given data

        Args:
            name (str): hotel name
            adress (str): hotel adress
            rooms (int): number of rooms
        """
        try:
            self.name = name
            self.adress = adress
            self.rooms = rooms
            self.avaliable_rooms = len(rooms)
        except TypeError:
            raise Exception('Missing arguments')

    def delete_hotel(self):
        """delete the current hotel data
        """
        self.name = None
        self.adress = None
        self.rooms = []
        self.reservations = {}
        self.avaliable_rooms = 0
        self.bussy_rooms = 0

    def display_hotel_info(self):
        """Prints the current hotel data
        """
        print(f'Hotel name: {self.name}')
        print(f'Hotel adress: {self.adress}')
        print(f'Hotel rooms: {self.rooms}')
        print(f'Hotel reservations: {self.reservations}')
        print(f'Hotel avaliable rooms: {self.avaliable_rooms}')
        print(f'Hotel bussy rooms: {self.bussy_rooms}')

    def modify_hotel_info(self, field_name, new_value):
        """Modifies a given hotel field for a new value

        Args:
            field_name (str): name of the field to modify
            new_value (str,int): nee value to assign
        """

        if field_name == 'name':
            self.name = new_value
        elif field_name == 'adress':
            self.adress = new_value
        elif field_name == 'rooms':
            self.rooms = new_value
            self.avaliable_rooms = self.rooms - len(self.reservations)

    def reserve_room(self, room_number: int, date: str, customer):
        """Reserves a room for a given customer and date

        Args:
            room_number (int): number of the room
            date (str): reservation date
            customer (_type_): customer making the reservation
        """
        self.reservations.update({room_number:
                                  {'date': date, 'customer': customer}})

    def cancel_reservation(self, room_number: int):
        """Cancel a reservation for a given room

        Args:
            room_number (int): number of the room
        """
        del self.reservations[room_number]
