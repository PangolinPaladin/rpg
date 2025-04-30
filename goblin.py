class Goblin: 
    def __init__(self, name, health, power):
        self.name = name 
        self.health = health
        self.power = power
    def attack(self, other_hero):
        print("The %s dashes forth, striking %s for %s damage! " % (self.name, knight.name, self.power))

mudrake = Goblin("Mudrake", "7", "2")

knight = Goblin("Knight", "10", "5")

mudrake.attack(knight)

