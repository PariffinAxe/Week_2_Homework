class Guest:

    def __init__(self, name, age, wallet, favourite_genre=""):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_genre = favourite_genre
        self.drunkeness = 0
        self.time_spent = 0
        self.vip = False

    
    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.drunkeness += drink.alcohol_level

    def sing_song(self,song):
        self.drunkeness -= round(song.length*1.5, 2)
        self.time_spent += song.length
        if self.drunkeness <= 0:
            self.drunkeness = 0

    def listen_to_song(self, song):
        self.drunkeness -= song.length
        self.time_spent += song.length
        if self.drunkeness <= 0:
            self.drunkeness = 0

    def upgrade_vip(self):
        self.vip = True




