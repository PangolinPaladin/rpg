class Pokemon:
    def __init__(self, name, hitpoints, strength,):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength
#technically don't need mudshot anymore, since the attack is phrased under
#strike, but it's still here. 
    def mudshot(self,opponent):
        print(f"{self.name} fires a dob of mud at {opponent.name} blinding them and doing {self.strength} damage")
    def strike(self,opponent):
        print("why")
        opponent.hitpoints -= self.strength
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

class Trainer(Pokemon):
    def __init__(self, name, hitpoints, strength):
        super().__init__(name, hitpoints, strength)
    def strike(self, opponent): 
        print(f"{self.name} uses Mudshot, firing a dob of mud at {opponent.name} blinding them and doing {self.strength} damage")

class Wild(Pokemon):
    def __init__(self, name, hitpoints, strength):
        super().__init__(name, hitpoints, strength)
    def strike(self, opponent):
        print(f"{self.name} uses Bug Bite, chomping down on {opponent.name}.")
# trainer pokemon
sandshrew = Pokemon("Sandshrew", 30, 6)
#trainer = Trainer("Sandshrew", "30", "6")

# wild pokemon
caterpie = Pokemon("Caterpie", 13, 2)
#wild = Wild("Caterpie", "13", "2")


#sandshrew.mudshot(caterpie)
# working so far! 

#need to make generic "skill" definition, then put the moves under the pokemon when defined. 

#sandshrew.mudshot(caterpie)
#caterpie.status()


#QUESTIONS 
#    I had restore calling health instead of hitpoints, but no error. How? 
