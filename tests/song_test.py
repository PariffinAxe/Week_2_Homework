import unittest

from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_2 = Song("American Idiot", "Green Day", "Indy", 3)

    def test_name(self):
        self.assertEquals("American Idiot", self.song_2.name)

    def test_artist(self):
        self.assertEquals("Green Day", self.song_2.artist)

    def test_genre(self):
        self.assertEquals("Indy", self.song_2.genre)

    def test_length(self):
        self.assertEquals(3, self.song_2.length)


    
