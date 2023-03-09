class Stats:
    def __init__(self):
        self.skillPoints = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.focus = 0
        self.perception = 0

    def pointAdd(self):
        self.skillPoints += 1

    def pointAssign(self, attribute):
        self.attribute = attribute
        print("self.${attribute}")

