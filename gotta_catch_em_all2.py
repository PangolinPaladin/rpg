#imports
from sandshrew import Pokemon
from sandshrew import Trainer
from sandshrew import Wild
import random

#trainer pokemon 
#sandshrew = Pokemon("Sandshrew", 30, 6)
trainer = Trainer("Sandshrew", 20, 6)
#wild pokemon 
#caterpie = Pokemon("Caterpie", 13, 2)
wild = Wild("Caterpie", 13, 2)
#print encounter scene




#choose pokemon




#print throw pokemon




#print moves/retreat/item
def main():
    while trainer.alive and wild.alive: 
#        print(f"Wow! a {caterpie.name} appeared out of the grass!" )
#        print(f"Oh no! the {caterpie.name} seems angry! ")
#        print()
#        print()
#       sandshrew.deploy(caterpie)

        print()
        print("You're up trainer!" )
        print()
        print(f"1. Attack {wild.name}")
        print("2. Items")
        print("3. Retreat")
        user_input = input()
        if user_input == "1":
                print()
                trainer.strike(wild)
                print()
                print()
                print("Watch out!")
                wild.strike(trainer)
                print()
                trainer.status()
                wild.status()
                print("__________________________________________")
                if not wild.alive:
                    print(f"The {wild.name} fainted. ")
                    #it's too late, I've been here too long, I don't know 
                    #Nothing works, parentheses, colon, nothing. 
                    #also tried false, like the hero solution. No.
        elif user_input == "2":
            trainer.restore()
            print("You used a health potion, Sandshrew feels much better.")
        elif user_input == "3":
            print("You got away safely")
            break

#current status 04.29.25 Everything working, except math involved in mudshot.
#needto have it code subtraction from hitpoints
#code attack for caterpie

# moving this to here, that way it prints once on startup, not every loop.

print(f"Wow! a {wild.name} appeared out of the grass!" )
print(f"Oh no! the {wild.name} seems angry! ")
print()
print()
trainer.deploy(wild)


#UGGHH FORGOT this had to be here. confused for so long. 
main()



#main




#


##Questions
#








