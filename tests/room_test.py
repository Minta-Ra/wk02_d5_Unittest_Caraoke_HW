import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        # Create Room object:
        self.room_1 = Room("Radio Star")
        self.room_2 = Room("The Singing Stop")

        # Create Guest object
        self.guest_1 = Guest("Martha Smith", 7.00)
        self.guest_2 = Guest("John Higins", 14.00)
        self.guest_3 = Guest("Rachel Blue", 10.00)

        # Create Song object
        self.song_1 = Song("Dancing in the Moonlight", 3.45)
        self.song_2 = Song("Dance Monkey", 3.56)
        self.song_3 = Song("We are The Chanpions", 3.11)


    def test_to_check_in_guest(self):
        expected = 1
        self.room_1.check_in_guest(self.guest_2)
        actual = self.room_1.num_of_guests()
        self.assertEqual(expected, actual)

    def test_to_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_2)
        expected = 0
        actual = self.room_1.num_of_guests()
        self.assertEqual(expected, actual)

    def test_songs_added_to_room(self):
        self.room_1.add_song_to_room(self.song_2)
        self.room_1.add_song_to_room(self.song_3)
        expected = 3
        actual = self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(expected, actual)

    def test_room_has_space__true(self):
        self.room_1.check_in_guest(self.guest_1)
        expected = True
        actual = self.room_1.check_room_space()
        self.assertEqual(expected, actual)

    def test_room_has_space__False(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        expected = False
        actual = self.room_1.check_room_space()
        self.assertEqual(expected, actual)

    def test_add_sold_ticket_fee_to_till(self):
        self.room_1.sell_ticket(self.guest_2, self.room_1)
        self.room_1.sell_ticket(self.guest_3, self.room_1)
        expected = 18.0
        actual = self.room_1.sell_ticket(self.guest_1, self.room_1)
        self.assertEqual(expected, actual)