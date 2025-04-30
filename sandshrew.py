class Pokemon:
    def __init__(self, name, hitpoints, strength,):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength
    def mudshot(self,opponent):
        print(f"{self.name} fires a dob of mud at {opponent.name} blinding them and doing {self.strength} damage")
        #opponent.hitpoints -= self.strength
    def alive(self):
        while self.hitpoints() > 0: 
            print(f"Good job {self.name}, keep it up!")
            
    def deploy(self,opponent):
            print("You throw your pokeball.")
            print(f"Go {self.name}! That {opponent.name} is no match for you! ")
    def restore(self): 
        self.hitpoints = 20
        print("Sandshrew's health is returned to full")
    def status(self):
        print(f"{self.name} has {self.hitpoints} hitpoints remaining.")

# trainer pokemon
sandshrew = Pokemon("Sandshrew", "30", "6")

# wild pokemon
caterpie = Pokemon("Caterpie", "13", "2")


#sandshrew.mudshot(caterpie)
# working so far! 

#need to make generic "skill" definition, then put the moves under the pokemon when defined. 

sandshrew.status()
caterpie.status()


#QUESTIONS 
#    I had restore calling health instead of hitpoints, but no error. How? 
