#imports
from sandshrew import Pokemon
import random

#trainer pokemon 
sandshrew = Pokemon("Sandshrew", "30", "6")

#wild pokemon 
caterpie = Pokemon("Caterpie", "13", "2")

#print encounter scene




#choose pokemon




#print throw pokemon




#print moves/retreat/item
def main():
    while sandshrew.alive and caterpie.alive: 
#        print(f"Wow! a {caterpie.name} appeared out of the grass!" )
#        print(f"Oh no! the {caterpie.name} seems angry! ")
#        print()
#        print()
#       sandshrew.deploy(caterpie)

        print()
        print("You're up trainer!" )
        print()
        print(f"1. Attack {caterpie.name}")
        print("2. Items")
        print("3. Retreat")
        user_input = input()
        if user_input == "1":
                print()
                sandshrew.mudshot(caterpie)
                print()
                print()
                print("Watch out!")
                caterpie.mudshot(sandshrew)
                sandshrew.status()
                caterpie.status()
                print("__________________________________________")
            #if not caterpie.alive():
            # s   print(f"The {opponent.name} fainted. ")
        elif user_input == "2":
            sandshrew.restore()
            print("You used a health potion, Sandshrew feels much better.")
        elif user_input == "3":
            print("You got away safely")
            break

#current status 04.29.25 Everything working, except math involved in mudshot.
#needto have it code subtraction from hitpoints
#code attack for caterpie

# moving this to here, that way it prints once on startup, not every loop.

print(f"Wow! a {caterpie.name} appeared out of the grass!" )
print(f"Oh no! the {caterpie.name} seems angry! ")
print()
print()
sandshrew.deploy(caterpie)


#UGGHH FORGOT this had to be here. confused for so long. 
main()



#main




#


##Questions
#








