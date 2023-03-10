class Stats:
    def __init__(self):
        self.skillPoints = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.focus = 0
        self.perception = 0
    
    def __repr__(self):
        print(f"Skill Points: {self.skillPoints}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")        
        print(f"Constitution: {self.constitution}")
        

    def pointAdd(self):
        self.skillPoints += 1

    def pointAssign(self, attribute : str):
        val = attribute
        if (val == "strength"):
            self.strength += 1
        elif (val == "dexterity"):
            self.dexterity += 1
        elif (val == "constitution"):
            self.constitution += 1
        elif (val == "intelligence"):
            self.intelligence += 1
        elif (val == "focus"):
            self.focus += 1
        elif (val == "perception"):
            self.perception += 1
        
        if (self.skillPoints > 0):
            self.skillPoints -= 1

        
        

