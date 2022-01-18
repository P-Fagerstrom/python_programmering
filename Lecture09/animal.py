class Animal:
    
    def __init__(self, species:str):
        self.species = species
        self.energy = 5

    def make_noise(self):
        self.energy -= 1
        print('*animal is making noise*')
        
    def feed(self):
        self.energy += 3
        
class Dog(Animal):
    
    def __init__(self):
        super().__init__(species='dog')
        
    
    def make_noise(self):
        self.energy -= 1
        print('Woof woof')
        
    def play(self):
        print('The dog is playing happily')
        self.energy -= 2