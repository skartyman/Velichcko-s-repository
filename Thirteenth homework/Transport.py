

class Transport:
    """
    Родительский класс, который описывает транспортное средство.
    Атрибуты:
        - name -> (str): название транспортного средства
        - max_speed -> (float): максимальная скорость транспортного средства в км/ч
        - fuel_type -> (str): тип топлива (например, бензин, дизель, электричество)
        - current_speed -> (float): текущая скорость транспортного средства в км/ч
        - license_plate -> (str): государственный регистрационный номер транспортного средства
        - engine_power -> (float): мощность двигателя в лошадиных силах
    Методы:
        - start(): запустить транспортное средство
        - stop(): остановить транспортное средство
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
    """

    def __init__(self, name, max_speed, fuel_type, license_plate, engine_power):
        self.name = name
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.current_speed = 0
        self.license_plate = license_plate
        self.__engine_power = engine_power

    def get_engine_power(self):
        """
        Получить мощность двигателя транспортного средства.
        """
        return self.__engine_power

    def set_engine_power(self, new_power):
        """
        Изменить мощность двигателя транспортного средства.
        """
        if new_power > 0:
            self.__engine_power = new_power

    def start(self):
        """
        Запустить транспортное средство.
        """
        self.current_speed = 10

    def stop(self):
        """
        Остановить транспортное средство.
        """
        self.current_speed = 0

    def accelerate(self, speed_increase):
        """
        Увеличить скорость на указанное значение.
        Параметры: - speed_increase (float): увеличение скорости в км/ч
        """
        self.current_speed += speed_increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed



class Bicycle(Transport):

    """
    Наследованный от класса Transport подкласс, который описывает велосипед.
    Атрибуты:
        - name -> (str): название велосипеда
        - max_speed -> (float): максимальная скорость велосипеда в км/ч
        - license_plate -> (str): государственный регистрационный номер велосипеда
        - engine_power -> (float): мощность двигателя в лошадиных силах (по умолчанию 0)
    Методы:
        - start(): запустить велосипед
        - stop(): остановить велосипед
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
    """

    def __init__(self, name, max_speed, license_plate, engine_power=0):
        super().__init__(name, max_speed, 'pedals', license_plate, engine_power)

    def start(self):
        """
        Старт велосипеда.
        """
        self.current_speed = 5

    def set_engine_power(self, engine_power):
        """
        Установить мощность двигателя велосипеда (не реализовано для велосипеда)
        """
        raise NotImplementedError("Велосипед не имеет двигателя")

    def get_engine_power(self):
        """
        Получить мощность двигателя велосипеда (не реализовано для велосипеда)
        """
        raise NotImplementedError("Велосипед не имеет двигателя")

class Car(Transport):
    """
    Наследованный от класса Transport подкласс, который описывает автомобиль.
    Атрибуты:
        - name -> (str): название автомобиля
        - max_speed -> (float): максимальная скорость автомобиля в км/ч
        - fuel_type -> (str): тип топлива (например, бензин, дизель, электричество)
        - license_plate -> (str): государственный регистрационный номер автомобиля
        - engine_power -> (float): мощность двигателя в лошадиных силах
    Методы:
        - start(): запустить автомобиль
        - stop(): остановить автомобиль
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
    """
    def __init__(self, name, max_speed, fuel_type, license_plate, engine_power):
        super().__init__(name, max_speed, fuel_type, license_plate, engine_power)

class Bus(Transport):
    """
    Наследованный от класса Transport подкласс, который описывает автобус.
    Атрибуты:
        - name -> (str): название автобуса
        - max_speed -> (float): максимальная скорость автобуса в км/ч
        - fuel_type -> (str): тип топлива (например, бензин, дизель, электричество)
        - license_plate -> (str): государственный регистрационный номер автобуса
        - engine_power -> (float): мощность двигателя в лошадиных силах
    Методы:
        - start(): запустить автобус
        - stop(): остановить автобус
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
    """
    def __init__(self, name, max_speed, fuel_type, license_plate, engine_power):
        super().__init__(name, max_speed, fuel_type, license_plate, engine_power)

class Truck(Car):
    """
    Наследованный от класса Car, который описывает грузовик.
    Атрибуты:
        - name -> (str): название грузовика
        - max_speed -> (float): максимальная скорость грузовика в км/ч
        - fuel_type -> (str): тип топлива (например, бензин, дизель, электричество)
        - license_plate -> (str): государственный регистрационный номер грузовика
        - engine_power -> (float): мощность двигателя в лошадиных силах
        - max_cargo_weight -> (float): максимальный вес груза в тоннах, который может перевозить грузовик
    Методы:
        - start(): запустить грузовик
        - stop(): остановить грузовик
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
        - load_cargo(weight: float): загрузить груз в грузовик
    """
    def __init__(self, name, max_speed, fuel_type, license_plate, engine_power, max_cargo_weight):
        super().__init__(name, max_speed, fuel_type, license_plate, engine_power)
        self.max_cargo_weight = max_cargo_weight
        self.current_cargo_weight = 0

    def load_cargo(self, weight):
        """
        Загрузить груз в грузовик.
        Проверяет, не превышает ли вес груза максимальный вес груза грузовика.
        Аргументы: - weight (float): вес груза в тоннах
        """
        if weight + self.current_cargo_weight > self.max_cargo_weight:
            raise ValueError(f"Невозможно загрузить груз весом {weight} тонн. Максимальный вес груза грузовика: {self.max_cargo_weight} тонн.")
        else:
            self.current_cargo_weight += weight


class Motorcycle(Bicycle):
    """
    Подкласс класса Bicycle, который описывает мотоцикл.
    Атрибуты:
        - name -> (str): название мотоцикла
        - max_speed -> (float): максимальная скорость мотоцикла в км/ч
        - fuel_type -> (str): тип топлива (например, бензин, дизель, электричество)
        - license_plate -> (str): государственный регистрационный номер мотоцикла
        - engine_power -> (float): мощность двигателя в лошадиных силах
    Методы:
        - start(): запустить мотоцикл
        - accelerate(speed_increase: float): увеличить скорость на указанное значение
    """
    def __init__(self, name, max_speed, fuel_type, license_plate, engine_power):
        super().__init__(name, max_speed, license_plate, engine_power)
        self.fuel_type = fuel_type
