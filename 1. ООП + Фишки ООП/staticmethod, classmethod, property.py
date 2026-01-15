class Temperature:
    def __init__(self, value): #тут в цельсия
        self.value = value

    @classmethod
    def degree_fahrenheit(cls, fahrenheit): 
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.value + 273.15
    
    @staticmethod
    def checking_for_freezing(temperature):
        return temperature < 0


temp_fahrenheit = Temperature.degree_fahrenheit(50)
print(f"Температура в градусах Цельсия из Фаренгейтов: {temp_fahrenheit.value}")


temp_celsius = Temperature(-10)
print(f"Температура в Кельвинах: {temp_celsius.kelvin}")


freezing_check = Temperature.checking_for_freezing(temp_celsius.value)
print(f"Температура {temp_celsius.value}°C замерзает: {freezing_check}")

#C = (°F — 32) × 5/9 - из цельсия в фаренгейта
#(K): K = °C + 273,15. - из цельсия в кельвины 