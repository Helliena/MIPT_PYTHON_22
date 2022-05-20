import time

class Cat:
    def __init__(self):
        self.satiety = 100
        self.satiety_last_update = time.time()
        self.satiety_update_speed = 0.5
        self.drunk = 100
        self.drunk_last_update = time.time()
        self.drunk_update_speed = 0.3
        self.chill = 100
        self.chill_last_update = time.time()
        self.chill_update_speed = 0.7
        self.sport = 100
        self.sport_last_update = time.time()
        self.sport_update_speed = 0.1

    def update(self):
        self.satiety = round(100 - (time.time() - self.satiety_last_update) * self.satiety_update_speed, 2)
        self.drunk = round(100 - (time.time() - self.drunk_last_update) * self.drunk_update_speed, 2)
        self.chill = round(100 - (time.time() - self.chill_last_update) * self.chill_update_speed, 2)
        self.sport = round(100 - (time.time() - self.sport_last_update) * self.sport_update_speed, 2)

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
    


