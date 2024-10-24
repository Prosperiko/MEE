#flexing my OOP powers with Prosper's module
import FuncModule
class  Animal:
    def __init__(self, name = 'Animal', colour = 'Brown', food = 'Bread', habitat = 'Land'):
        self.name = name
        self.colour = colour
        self.habitat = habitat
        
    def walk(self,speed = 5, ):
        self.speed = Multi(speed)
        import time
        for i in range (self.speed):
            time.sleep(0.5)
            print(f'{self.name} moved {i} step')
            
        print(f'{self.name} has arrived {self.food}')
        
        
