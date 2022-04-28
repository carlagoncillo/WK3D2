class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food,):
        self.name = first_name
        self.last = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet('Dodong', 'Joseph', 'Angkol')
    
    def walk(self):
        self.pet.play()
        print('Walking with Dodong')

    def feed(self):
        self.pet.eat()
        print('Dodong is Eating')

    def bathe(self):
        self.pet.noise()
        print('Bathing Dodong')

class Pet:
    def __init__(self, name, dogtype, tricks):
        self.name = name
        self.type = dogtype
        self.tricks = tricks
        self.health = 20
        self.energy = 50
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5 
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self
        
    def noise(self):
        print('WOOOF WOOOF')

carl = Ninja('Carl', 'Agoncillo', 'Blackberry', 'Banana')
carl.walk()
carl.bathe()
carl.feed()