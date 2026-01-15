from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start_engine():
        pass


    @abstractmethod
    def stop_engine():
        pass


    @abstractmethod
    def move():
        pass

class Car(Transport):
    def __init__(self, speed):
        self.speed = speed

    def start_engine(self):
        return 'поехала'

    def stop_engine(self):
        return 'перестала ехать'

    def move(self):
        return f' машина едет {self.speed} км/ч'
    

class Boat(Transport):
    def __init__(self, speed):
        self.speed = speed

    def start_engine(self):
        return 'поехала'

    def stop_engine(self):
        return 'перестала ехать'

    def move(self):
        return f' лодка едет {self.speed} км/ч'



exm1 = Car(100)
check = exm1.move()
print(check)


exm2 = Boat(30)
check2 = exm2.move()
print(check2)

