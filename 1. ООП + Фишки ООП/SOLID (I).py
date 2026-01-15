from abc import ABC, abstractmethod

class Can_fly(ABC):
    @abstractmethod
    def fly(self):
        pass

class Can_run(ABC):
    @abstractmethod
    def run(self):
        pass

class Can_swim(ABC):
    @abstractmethod
    def swim(self):
        pass


class Lion(Can_run):
    def run(self):
        print('lion runs')


l = Lion()
l.run()