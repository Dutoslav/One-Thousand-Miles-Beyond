import random

terrain_types = {"plain":0.9, "hill":1.1, "down hill":0.8, "mountain":1.3, "down mountain":1, "swamp":1.1, "forest":1}
terrain = ["plain", "hill", "down hill", "mountain", "down mountain", "swamp", "forest"]

class Player:
    def __init__(self, name = "Player"):
        self.name = name
        self.distance = 0
        self.fatigue = 0

    def walk(self, terrain, km):
        self.distance += km
        self.fatigue += (km*1) * terrain_types[terrain]
        print("You travelled {} kms. In total you travelled {}/100 kms. Your current fatigue is {}/100".format(km, self.distance, round(self.fatigue, 2)))
        if self.fatigue > 100:
            print("Dead")
            exit()
            

player = Player()
player.name = input("Enter your name:")
print("Your goal is 100kms away, you better start walking.")

while player.distance < 100:
    dir1 = terrain[random.randrange(0,5)]
    dir2 = terrain[random.randrange(0,5)]
    dir3 = terrain[random.randrange(0,5)]
    if (100 - player.distance) > 14: 
        distance = random.randrange(3,15)
    else:
        distance = 100 - player.distance
    print("1. {} \n2. {}\n3. {}".format(dir1, dir2, dir3))
    dir = input("Type the direction you wish to travel:")
    player.walk(dir, distance)

if player.distance >= 100 and player.fatigue < 100:
    print("Congratulations, you have reached your goal.")