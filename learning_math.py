class Hero:
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
        return hero.health
    def __add__(self):
        pass
    def hitpoints (int(hero.health)):
        return hero.hitpoints


bob = Hero("Bob", "10", "5")

bob.__add__("bob.power", "bob.health")

#status: in order to do math, python requires that they be defined 
       # as integers or floats. So where do I put in my class that these are integers 

#int(string) should report something as a string

y += 1			# add then assign value

y -= 1			# subtract then assign value

y *= 2			# multiply then assign value

y /= 3			# divide then assign value

y // = 5		# floor divide then assign value

y **= 2			# increase to the power of then assign value

y %= 3			# return remainder then assign value