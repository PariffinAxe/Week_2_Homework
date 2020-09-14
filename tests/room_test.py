import unittest
import pdb

from src.room import *
from src.song import *
from src.guest import *
from src.drink import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(5, 10, 10, 16, 200, "Rock", "Metal")
        self.room_2 = Room(20, 15, 20, 18, 400, "Pop", "Disco", "R&B")
        self.room_3 = Room(10, 5, 3, 20, 150, "Indy", "Alternative")
        self.drink_1 = Drink("Beer", 120, 5)
        self.drink_2 = Drink("Wine", 180, 9)
        self.drink_3 = Drink("Coke", 0, 1.50)
        self.song_1 = Song("Ain't My Fault", "Zara Larsson", "Pop", 3.75)
        self.song_2 = Song("American Idiot", "Green Day", "Indy", 3)
        self.song_3 = Song("Alarm", "Anne-Marie", "Disco", 3.5)
        self.song_4 = Song("American", "Green", "R&B", 4)
        self.song_5 = Song("Idiot", "Day", "Pop", 5)
        self.song_6 = Song("Yellow", "Coldplay", "Pop", 2.5)
        self.song_7 = Song("The People", "Wanted", "Pop", 2.5)
        self.song_list = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6, self.song_7]
        self.guest_1 = Guest("Edyta", 43, 30, "Rock")
        self.guest_2 = Guest("Bob", 17, 20)
        self.guest_3 = Guest("James", 15, 30, "Pop")
        self.guest_4 = Guest("Joseph", 20, 3)
        self.guest_5 = Guest("Margeret", 19, 30)
        self.guest_6 = Guest("Mike", 42, 20)
        self.guest_7 = Guest("Ryan", 40, 25)
        self.guest_8 = Guest("Aidan", 38, 25)
        

    def test_max_occupancy(self):
        self.assertEquals(5, self.room_1.max_occupancy)

    def test_entry_fee(self):
        self.assertEquals(10, self.room_1.entry_fee)

    def test_upgrade_price(self):
        self.assertEquals(20, self.room_2.upgrade_price)

    def test_min_age(self):
        self.assertEquals(16, self.room_1.min_age)

    def test_till(self):
        self.assertEquals(200, self.room_1.till)

    def test_3_genres(self):
        self.assertEquals(3, len(self.room_2.genres))

    def test_2_genres(self):
        self.assertEquals(2, len(self.room_1.genres))

    def test_add_drink(self):
        self.room_1.add_drink_to_stock(self.drink_1)
        self.assertEquals(1, len(self.room_1.drinks))

    def test_add_multiple_drinks(self):
        self.room_1.add_drink_to_stock(self.drink_1)
        self.room_1.add_drink_to_stock(self.drink_1)
        self.room_1.add_drink_to_stock(self.drink_1)
        self.room_1.add_drink_to_stock(self.drink_2)
        self.room_1.add_drink_to_stock(self.drink_2)
        self.room_1.add_drink_to_stock(self.drink_3)
        self.assertEquals(3, self.room_1.check_available_stock(self.drink_1))
        self.assertEquals(2, self.room_1.check_available_stock(self.drink_2))
        self.assertEquals(1, self.room_1.check_available_stock(self.drink_3))

    def test_open_room(self):
        self.room_2.open_room(self.song_list)
        self.assertEquals(6, len(self.room_2.available_songs))
    
    def test_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEquals(1, len(self.room_1.guest_list))

    def test_dont_add_age(self):
        self.room_1.add_guest(self.guest_3)
        self.assertEquals(0, len(self.room_1.guest_list))

    def test_dont_add_cant_afford(self):
        self.room_1.add_guest(self.guest_4)
        self.assertEquals(0, len(self.room_1.guest_list))

    # def test_dont_add_no_space(self):
    #     pdb.set_trace()
    #     self.room_1.add_guest(self.guest_1)
    #     self.room_1.add_guest(self.guest_2)
    #     self.room_1.add_guest(self.guest_5)
    #     self.room_1.add_guest(self.guest_6)
    #     self.room_1.add_guest(self.guest_7)
    #     self.room_1.add_guest(self.guest_8)
    #     self.assertEquals(5, len(self.room_1.guest_list))    

    def test_upgrade_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.upgrade_guest(self.guest_1)
        self.assertEquals(1, len(self.room_1.vip_guest_list))

    # def test_cant_upgrade_cost(self):
    #     self.room_2.add_guest(self.guest_7)
    #     self.room_2.upgrade_guest(self.guest_7)
    #     self.assertEquals(0, len(self.room_2.vip_guest_list))

    def test_song_available(self):
        self.room_2.open_room(self.song_list)
        self.assertEquals(True, self.room_2.song_available(self.song_1))

    def test_song_not_available(self):
        self.room_3.open_room(self.song_list)
        self.assertEquals(False, self.room_3.song_available(self.song_1))

    def test_add_song(self):
        self.room_2.open_room(self.song_list)
        self.room_2.add_guest(self.guest_1)
        self.room_2.add_song_to_queue(self.song_1, self.guest_1)
        self.assertEquals(1, len(self.room_2.song_queue))

    def test_multiple_songs_and_vip(self):
        self.room_2.open_room(self.song_list)
        self.room_2.add_guest(self.guest_1)
        self.room_2.add_guest(self.guest_2)
        self.room_2.upgrade_guest(self.guest_1)
        self.room_2.add_song_to_queue(self.song_1, self.guest_1)
        self.room_2.add_song_to_queue(self.song_3, self.guest_1)
        self.room_2.add_song_to_queue(self.song_5, self.guest_2)
        self.assertEquals(1, len(self.room_2.song_queue))
        self.assertEquals(2, len(self.room_2.vip_song_queue))
        
    def test_next_song(self):
        self.room_2.open_room(self.song_list)
        self.room_2.add_guest(self.guest_1)
        self.room_2.add_guest(self.guest_2)
        self.room_2.upgrade_guest(self.guest_1)
        self.guest_1.drunkeness = 100
        self.guest_2.drunkeness = 100
        self.room_2.add_song_to_queue(self.song_1, self.guest_1)
        self.room_2.add_song_to_queue(self.song_3, self.guest_1)
        self.room_2.add_song_to_queue(self.song_5, self.guest_2)
        self.room_2.next_song()
        self.assertEquals(1, len(self.room_2.song_queue))
        self.assertEquals(1, len(self.room_2.vip_song_queue))
        self.assertEquals(1, len(self.room_2.song_break_queue))
        self.assertEquals(3, len(self.room_2.available_songs))
        self.assertEquals(94.38, self.guest_1.drunkeness)
        # self.assertEquals(96.25, self.guest_2.drunkeness)
        self.assertEquals(3.75, self.guest_1.time_spent)
        # self.assertEquals(3.75, self.guest_2.time_spent)

    def test_remove_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEquals(0, len(self.room_1.guest_list))

    def test_remove_vip_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.upgrade_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEquals(0, len(self.room_1.vip_guest_list))
        


       