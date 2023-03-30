class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeuecats(self):
        if not self.cats:
            return None
        return self.cats.pop(0)

    def dequeuedogs(self):
        if not self.dogs:
            return None
        return self.dogs.pop(0)

    def dequeueany(self):
        if not self.cats:
            return self.dogs.pop(0)
        return self.cats.pop(0)


shelter = AnimalShelter()
shelter.enqueue('cat1', 'cat')
shelter.enqueue('cat2', 'cat')
shelter.enqueue('dog1', 'dog')
shelter.enqueue('cat3', 'cat')
shelter.enqueue('dog2', 'dog')
print(shelter.dequeuecats())
print(shelter.dequeuedogs())
print(shelter.dequeuecats())
print(shelter.dequeuecats())
print(shelter.dequeueany())