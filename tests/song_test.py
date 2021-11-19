import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        # Create Song object
        self.song_1 = Song("Dancing in the Moonlight", 3.45)


    def test_song_has_length(self):
        expected = 3.45
        actual = self.song_1.length
        self.assertEqual(expected, actual)