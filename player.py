import math

class Player():
        def __init__(self):
            self.levels = 0.00
            
            
        
        def level(self, type, amount):
            def xptolevel(xp):
                temp = 2 * math.pow(xp, (1/3))
                return temp  
            amount = xptolevel(amount)
            try:
                if type == '-':
                    self.levels -= amount
                elif type == '+':
                    self.levels += amount
                else:
                    raise Exception 
            except:
                print("Invalid Parameter: ", type)

        def getLevel(self):
             return int(self.levels)
        def getLevelStatus(self):
            return '{:.2f}'.format(self.levels)   
        
              

me = Player()
me.level('+', 15)
print(me.getLevel())
print(me.getLevelStatus())

