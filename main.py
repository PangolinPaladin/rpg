#First we pull our classes from their files
from hero import Hero
#from goblin import Goblin

knight = Hero("Knight", "10", "5")

mukluk = Hero("Mukluk", "6", "2")

 #probably want this somewhere else but for now it's here

def print_menu_error():
    print("Hero! What is your command? \n\n\n")
# QUESTION: What do these n's do? \

# I would love to put attack in a class, but what would the second variable be? in the contacts excercise it was other person, 
# but I need to reference two classes. Goblin and Hero
## I see now. goblin.attack(hero), but hero wont be defined?

#Heroes attack (not using currently)
#def heroes_attack(self, goblin):
#    print("%s's sword flashes across, cleaving into %s " % (knight.name, mudrake.name))

#Goblins attack (Not currently using)
#def goblins_stab(self, hero):
#    print("The cunning %s slides forward, finding purchase between %s's armor with his rusty dagger" % (mudrake.name, knight.name))



# This needs to be changed to referece my classes, hero and goblin, specifically hero. 
def main():
    knight.health
    knight.power
    mukluk.health
    knight.power

while knight.alive and mukluk.alive:
        print("You have %s health and %s power." % (knight.health, knight.power))
        print("The goblin has %s health and %s power." % (mukluk.health, mukluk.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            knight.attack(mukluk)
            print("You do %s damage to the %s." % (knight.power,mukluk.name))
            if mukluk.alive:
                print("The enemy still stands!" )
            if not mukluk.alive: 
                print("You have slain the foe!" )
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if mukluk.alive:
            # Goblin attacks hero
            knight.health - mukluk.power
            print("The goblin does %s damage to you." % (mukluk.power))
            if not knight.alive
                print("You are dead.")



#main menu
#input function showing the user the menu and having them choose 1,2, or 3, with a error for other options


#Current Status: doing math in functions. Strings aren't "numbers", so int? Lot of changing if that is the case. 
# cheated at this point and looked at solution, the solution has no math? Moving to stage two