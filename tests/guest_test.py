import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        # Create Gusest object
        self.guest_1 = Guest("Martha Smith", 10.00)


    def test_guest_has_name(self):
        expected = "Martha Smith"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)