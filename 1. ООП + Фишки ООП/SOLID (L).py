from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def say_hi(self):
        pass

class Sparrow(Bird):
    def __init__(self, speed: int):
        self.speed = speed

    def say_hi(self):
        print(f'hi im sparrow and my speed = {self.speed} км/ч') 



class Penguin(Bird):
    def __init__(self, mind: str):
        self.mind = mind

    def say_hi(self):
        print(f'hi im penguin and my mind so {self.mind}')


s = Sparrow(35)
p = Penguin('sharp')

s.say_hi()
p.say_hi()

# birds = [s,p]
# for bird in birds:
#     bird.say_hi()
