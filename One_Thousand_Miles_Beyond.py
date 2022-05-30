terrain_types = {plains:1, hills:1.2, down_hill:0.9}


class Player:
    def __init__(self, name = "Player", distance, fatigue):
        self.name = name
        self.distance = 0
        self.fatigue = 0

    def walk(self, terrain, km):
        self.distance += km
        self.fatigue += (km*0.5) * terrain_types[terrain]
        if fatigue > 100:
            print("Dead")
        print("You travelled {km} kms".format(km))