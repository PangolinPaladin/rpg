class Hero:
    def __init__(self, name, health, power, coins):
        self.name = name 
        self.health = health
        self.power = power
        self.coins = coins
    def attack(self, other_hero):
        print("The %s dashes forth, striking %s for %s damage! " % (self.name, kobold.name, self.power))
    def alive(self):
        while self.health > 0:
            print("You're still standing!")
    def print_status():
        return hero.health
    #def hitpoints(int(4)):
        print(knight.hitpoints)

#finally figured out the math problem. python not oops. here goes. 
    def attack_result(self):
        print(knight.health - knight.power)



knight = Hero("Knight", "20", "10", "3")

kobold = Hero("Kobold", "15", "8", "1")

knight.attack(kobold)



#print(hitpoints ** hitpoints)

knight.attack_result
# this doesn't throw a code, but doesn't print. Don't remember why. 

#okay. So int works for a simple function as above. why wont it work for what I need?

