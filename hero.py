class Hero:
    def __init__(self, name, health, power, coins):
        self.name = name 
        self.health = health
        self.power = power
        self.coins = coins
    def attack(self, other_hero):
        print("The %s dashes forth, striking %s for %s damage! " % (self.name, goblin.name, self.power))
    def alive(self):
        while self.health > 0:
            print("You're still standing!")
    def print_status():
        return hero.health
#This is a dirty way to do this, doesn't mention the other class. 



knight = Hero("Knight", "10", "5", "20")

goblin = Hero("Mukluk", "6", "2", "0")


#This won't run with the goblins name as the variable in parentheses


#Should this and goblin be under a class, with these being subclasses? Options? 
# QUESTION: Can you leave something undefined? Sometimes the hero will attack a goblin, sometimes a skeleton
