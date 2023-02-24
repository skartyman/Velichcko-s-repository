from Transport import *

# Создание объекта класса Bicycle
bike = Bicycle("Azimut", 40.0, "Manual", "0001")

# Создание объекта класса Car
car = Car("Toyota Corolla", 180.0, "Gasoline", "1234 AA-7", 140.0)

# Создание объекта класса Bus
bus = Bus("Neoplan", 100.0, "Diesel", "5678 BB-7", 250)

# Создание объекта класса Motorcycle
moto = Motorcycle("Harley Davidson", 200.0, "Gasoline", "4321 CC-7", 80.0)

# Создание объекта класса Truck
truck = Truck("Scania", 80.0, "Diesel", "9999 ZZ-7", 400.0, 5000)

# Использование методов классов
bike.start()
car.accelerate(20.0)
bus.stop()
moto.start()
truck.load_cargo(5000)
truck.set_engine_power(800.0)
