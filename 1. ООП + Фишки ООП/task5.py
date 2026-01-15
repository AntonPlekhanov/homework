class Flyable:
    def fly(self):
        return "i'm flying!"

class Swimmable:
    def swim(self):
        return "I'm swimming!"

class Duck(Flyable, Swimmable):
    def make_sound(self):
        return 'Quack!'


d = Duck()
check = d.make_sound()
print(check)

s = Duck()
check = s.swim()
print(check)

f = Duck()
check = f.fly()
print(check)