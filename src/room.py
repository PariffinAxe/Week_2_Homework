class Room:
    def __init__(self, max_occupancy, entry_fee, vip_upgrade_fee, min_age, till, genre_1, genre_2, genre_3=""):
        self.max_occupancy = max_occupancy
        self.max_vips = round(max_occupancy*0.4, 0)
        self.entry_fee = entry_fee
        self.upgrade_price = vip_upgrade_fee
        self.min_age = min_age
        self.till = till
        self.genres = [genre_1, genre_2, genre_3] if genre_3 != "" else [genre_1, genre_2]
        self.available_songs = []
        self.vip_song_queue = []
        self.song_queue = []
        self.song_break_queue = []
        self.guest_list = []
        self.vip_guest_list = []
        self.drinks = {}
    
    
    
    def add_drink_to_stock(self, drink):
        if drink in self.drinks:
            self.drinks[drink] += 1
        else:
            self.drinks[drink] = 1

    def check_available_stock(self,drink):
        if drink in self.drinks:
           return self.drinks[drink]
        else:
            return 0
    
    def open_room(self, song_list):
        for song in song_list:
            if song.genre in self.genres:
                self.available_songs.append(song)

    def check_if_space_left(self):
        if len(self.guest_list) < self.max_occupancy:
            return True

    def guest_can_afford_entry(self, guest):
        return guest.wallet >= self.entry_fee

    def guest_old_enough(self, guest):
        return guest.age >= self.min_age

    def add_guest(self, guest):
        if self.check_if_space_left and self.guest_can_afford_entry(guest) and self.guest_old_enough(guest):
            self.guest_list.append(guest)
            self.till += self.entry_fee
            guest.wallet -= self.entry_fee

    def check_if_vip_space(self):
        return self.max_vips > len[self.vip_guest_list]

    def guest_can_afford_upgrade(self, guest):
        return guest.wallet >= self.upgrade_price
    
    def upgrade_guest(self, guest):
        if self.check_if_vip_space and self.guest_can_afford_upgrade:
            self.vip_guest_list.append(guest)
            self.till += self.upgrade_price
            guest.wallet -= self.upgrade_price
            guest.upgrade_vip()

    def song_available(self,song):
        return song in self.available_songs

    def add_song_to_queue(self,song,guest):
        if self.song_available:
            self.available_songs.remove(song)
            song_singer = {"song":song, "singer":guest}
            self.vip_song_queue.append(song_singer) if guest.vip else self.song_queue.append(song_singer)
       
    def check_if_song_queue(self):
        return len(self.vip_song_queue) > 0 or len(self.song_queue) > 0
    
    def next_song(self):
        if self.check_if_song_queue:
            if len(self.vip_song_queue) > 0:
                song = self.vip_song_queue[0]["song"]
                singer = self.vip_song_queue[0]["singer"]
                self.vip_song_queue.pop(0)
            else:
                song = self.song_queue[0]["song"]
                sinher = self.song_queue[0]["singer"]
                self.song_queue.pop(0)
            self.song_break_queue.append(song)
            if len(self.song_break_queue) > 5:
                self.available_songs.append(self.song_break_queue[0])
                self.song_break_queue.pop(0)
            singer.sing_song(song)
            for guest in self.guest_list:
                if guest != singer:
                    guest.listen_to_song(song)
    

    def remove_guest(self, guest):
        if guest.vip:
            self.vip_guest_list.remove(guest)
        self.guest_list.remove(guest)

