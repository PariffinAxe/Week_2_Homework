import unittest

from src.guest import *
from src.drink import *
from src.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Edyta", 43, 30, "Rock")
        self.guest_2 = Guest("Bob", 17, 20)
        self.song_1 = Song("Ain't My Fault", "Zara Larsson", "Pop", 3.75)


    def test_name(self):
        self.assertEquals("Edyta", self.guest.name)

    def test_age(self):
        self.assertEquals(43, self.guest.age)

    def test_vip(self):
        self.assertEquals(False, self.guest.vip)

    def test_wallet(self):
        self.assertEquals(30, self.guest.wallet)

    def test_favourite_genre(self):
        self.assertEquals("Rock", self.guest.favourite_genre)
    
    def test_no_fav_genre(self):
        self.assertEquals("", self.guest_2.favourite_genre)

    def test_has_drunkeness(self):
        self.assertEquals(0, self.guest.drunkeness)

    def test_time_spent(self):
        self.assertEquals(0, self.guest.time_spent)

    def test_buy_alcoholic_drink(self):
        drink = Drink("Beer", 120, 5)
        self.guest.buy_drink(drink)
        self.assertEquals(120, self.guest.drunkeness)
        self.assertEquals(25, self.guest.wallet)

    def test_buy_non_alcoholic(self):
        drink = Drink("Coke", 0, 1.50)
        self.guest.buy_drink(drink)
        self.assertEquals(0, self.guest.drunkeness)
        self.assertEquals(28.50, self.guest.wallet)

    def test_sing_song_drunk(self):
        self.guest.drunkeness = 100
        self.guest.sing_song(self.song_1)
        self.assertEquals(94.38, self.guest.drunkeness)

    def test_sing_song_little_drunkeness(self):
        self.guest.drunkeness = 3
        self.guest.sing_song(self.song_1)
        self.assertEquals(0, self.guest.drunkeness)

    def test_sing_song_no_drunkeness(self):
        self.guest.sing_song(self.song_1)
        self.assertEquals(0, self.guest.drunkeness)

    def test_listen_to_song_drunk(self):
        self.guest.drunkeness = 100
        self.guest.listen_to_song(self.song_1)
        self.assertEquals(96.25, self.guest.drunkeness)

    def test_listen_to_song_little_drunk(self):
        self.guest.drunkeness = 2
        self.guest.listen_to_song(self.song_1)
        self.assertEquals(0, self.guest.drunkeness)

    def test_listen_to_song_not_drunk(self):
        self.guest.listen_to_song(self.song_1)
        self.assertEquals(0, self.guest.drunkeness)

    def test_upgrade_vip(self):
        self.guest.upgrade_vip()
        self.assertEquals(True, self.guest.vip)


