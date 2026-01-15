from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass



class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass



class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "бегает"


class Bird(Animal, Flyable):
    def speak(self):
        return "Tweet!"

    def move(self):
        return self.fly()
    
    def fly(self):
        return 'летает'


class Fish(Animal, Swimmable):
    def speak(self):
        return 'молчит'

    def move(self):
        return self.swim()
    
    def swim(self):
        return 'плавает'
    

animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.speak() + ' ' + animal.move())



#бегает
#летает
#плавает

#Woof! бегает
#Tweet! летает
#молчит плавает