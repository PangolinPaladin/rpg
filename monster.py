class Monster:
    def __init__(self, name, health, power):
        self.name = name 
        self.health = health
        self.power = power
    def attack(self, other_hero):
        print("The %s dashes forth, striking %s for %s damage! " % (self.name, goblin.name, self.power))
    def alive(self):
        while self.health > 0:
            print("You're still standing!")
    def print_status():
        return monster.health



#Trying again to master subclasses for additional monster types 

class Shadow(Monster):
    pass
necromorph = Shadow("Necromorph", 1, 4)
print(necromorph.power)
