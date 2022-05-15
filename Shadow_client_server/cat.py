import time
from collections import defaultdict

from numpy import character


class Cat:
    def __init__(self):
        self.satiety = 100
        self.satiety_last_update = time.time()
        self.drunk = 100
        self.drunk_last_update = time.time()
        self.chill = 100
        self.chill_last_update = time.time()
        self.sport = 100
        self.sport_last_update = time.time()

    def update(self):
        self.satiety = round(100 - (time.time() - self.satiety_last_update) * 0.5, 2)
        self.drunk = round(100 - (time.time() - self.drunk_last_update) * 0.3, 2)
        self.chill = round(100 - (time.time() - self.chill_last_update) * 0.7, 2)
        self.sport = round(100 - (time.time() - self.sport_last_update) * 0.1, 2)

    def eat(self):
        self.satiety_last_update = time.time()
    def drink(self):
        self.drunk_last_update = time.time()
    def go_chill(self):
        self.chill_last_update = time.time()
    def do_sport(self):
        self.sport_last_update = time.time()
    
    def watch(self):
        self.update()
        chr = {'satiety' : self.satiety, 'drunk' : self.drunk,
                'chill' : self.chill, 'sport' : self.sport}
        return dict(chr)
    


