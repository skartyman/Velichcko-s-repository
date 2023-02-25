from Transport import *
from Animals import *

# Создание объектов классов Transport
bike = Bicycle("Azimut", 40.0, "Manual", "0001")
car = Car("Toyota Corolla", 180.0, "Gasoline", "1234 AA-7", 140.0)
bus = Bus("Neoplan", 100.0, "Diesel", "5678 BB-7", 250)
moto = Motorcycle("Harley Davidson", 200.0, "Gasoline", "4321 CC-7", 80.0)
truck = Truck("Scania", 80.0, "Diesel", "9999 ZZ-7", 400.0, 5000)

# Использование методов классов
bike.start()
car.accelerate(20.0)
bus.stop()
moto.start()
truck.load_cargo(5000)
truck.set_engine_power(800.0)

# Вывод атрибутов объектов
print(f"Максимальная скорость {bike.name}: {bike.max_speed} км/ч.")
print(f"Топливо которое использует {bus.name}: {bus.fuel_type}.")
print(f"Максимальная грузоподъемность {truck.name}: {truck.max_cargo_weight}.")


# Создание объектов классов Animal
eagle1 = Eagle("Орел-белохвост", 3.5, 120, 2.3, 5000, 10, "зайцы")
penguin1 = Penguin("Пингвин", 1.2, 10, 1.5)
snake1 = Snake("Уж", 1.5, 15, 2.2, True)
lizard1 = Lizard("Лягушка", 0.5, 5, 3, False)
lion1 = Carnivore("Лев", 200, 80, "Саванна", 4, "антилопы")
elephant1 = Herbivore("Слон", 5000, 30, "Лес", 4, "растительная пища")

# Изменение скорости объекта
eagle1.speed = 150

# Использование методов классов
eagle1.hunt()
penguin1.swim()
snake1.crawl()
lizard1.swim()
lion1.hunt()
elephant1.graze()

# Вывод атрибутов объектов
print(f"Размах крыльев {eagle1.name}: {eagle1.wingspan} метра.")
print(f"Скорость {lion1.name}: {lion1.speed} км/ч.")
print(f"Количество лап {elephant1.name}: {elephant1.number_of_legs}.")
