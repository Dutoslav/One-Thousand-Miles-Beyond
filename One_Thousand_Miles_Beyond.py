import random

terrain_types = {"plains":1, "hills":1.2, "down_hill":0.9}
terrain = ["plains", "hills", "down_hill"]

class Player:
    def __init__(self, name = "Player"):
        self.name = name
        self.distance = 0
        self.fatigue = 0

    def walk(self, terrain, km):
        self.distance += km
        self.fatigue += (km*1) * terrain_types[terrain]
        if self.fatigue > 100:
            print("Dead")
        print("You travelled {} kms. In total you travelled {}/100 kms. Your current fatigue is {}/100".format(km, self.distance, self.fatigue))

player = Player()
player.name = input("Enter your name:")
print("Your goal is 100kms away, you better start walking.")

while player.distance < 100 or player.fatigue < 100 :
    dir1 = terrain[random.randrange(0,2)]
    dir2 = terrain[random.randrange(0,2)]
    distance = random.randrange(3,15)
    print("1. {} \n2. {}".format(dir1, dir2))
    dir = input("Type the direction you wish to travel:")
    player.walk(dir, distance)

if player.distance >= 100:
    print("Congratulations, you have reached your goal.")