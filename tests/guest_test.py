import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        # Create Gusest object
        self.guest_1 = Guest("Martha Smith", 10.00)

        # Create Room object:
        self.room_1 = Room("Radio Star")


    def test_guest_has_name(self):
        expected = "Martha Smith"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)

    def test_deduct_ticket_fee_from_wallet__can_afford(self):
        expected = 4.00
        actual = self.guest_1.deduct_ticket_fee_from_wallet(self.room_1)
        self.assertEqual(expected, actual)

    def test_deduct_ticket_fee_from_wallet__cannot_afford(self):
        self.guest_1.deduct_ticket_fee_from_wallet(self.room_1)
        expected = "Not enough money to buy a ticket"
        actual = self.guest_1.deduct_ticket_fee_from_wallet(self.room_1)
        self.assertEqual(expected, actual)