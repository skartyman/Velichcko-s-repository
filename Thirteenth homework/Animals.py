class Animal:
    """
    Класс, описывающий животное.
    Атрибуты:
        - name -> (str): название животного
        - weight -> (float): вес животного в килограммах
        - speed -> (float): скорость передвижения животного в км/ч
    Методы:
        - say(): издать звук, типичный для данного вида животных
        - move(): двигаться в соответствии со своими физиологическими особенностями
        - eat(): питаться, соответственно рациону
        - sleep(): спать, соответственно суточному режиму
    """

    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.__speed = speed

    def say(self):
        """
        Издать звук, типичный для данного вида животных.
        """
        pass

    def move(self):
        """
        Двигаться в соответствии со своими физиологическими особенностями.
        """
        pass

    def eat(self):
        """
        Питаться, соответственно рациону.
        """
        pass

    def sleep(self):
        """
        Спать, соответственно суточному режиму.
        """
        pass

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed < 0:
            print("Скорость не может быть отрицательной")
        else:
            self.__speed = new_speed



class Birds(Animal):
    """
    Подкласс класса Animal, который описывает птиц.
    Атрибуты:
        - wingspan (float): размах крыльев в метрах
        - flight_altitude (float): максимальная высота полета в метрах
    Методы:
        - fly(): птица взлетает и начинает летать
        - build_nest(): птица строит гнездо для откладывания яиц
    """
    def __init__(self, name, weight, speed, wingspan, flight_altitude):
        super().__init__(name, weight, speed)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def fly(self):
        """
        Птица взлетает и начинает летать.
        """
        print(f"{self.name} взлетает и начинает летать.")

    def build_nest(self):
        """
        Птица строит гнездо для откладывания яиц.
        """
        print(f"{self.name} строит гнездо для откладывания яиц.")



class Reptile(Animal):
    """
    Подкласс класса Animal - рептилии.
    Атрибуты:
        - has_scales -> (bool): наличие чешуи
        - is_poisonous -> (bool): ядовитость
    Методы:
        - crawl(): ползать
        - swim(): плавать
    """

    def __init__(self, name, weight, speed, is_poisonous):
        super().__init__(name, weight, speed)
        self.is_poisonous = is_poisonous

    def crawl(self):
        """
        Ползать.
        """
        pass

    def swim(self):
        """
        Плавать.
        """
        pass


class Snake(Reptile) :
    def __init__(self, name, weight, speed, length, is_poisonous):
        super().__init__(name, weight, speed, is_poisonous)
        self.length = length


class Lizard(Reptile) :
    def __init__(self, name, weight, speed, age, is_poisonous):
        super().__init__(name, weight, speed, is_poisonous)
        self.age = age

class Mammals(Animal):
    """
    Подкласс класса Animal, описывающий млекопитающих.
    Атрибуты:
        - fur_type -> (str): тип меха у млекопитающего
        - habitat -> (str): место обитания млекопитающего
        - number_of_legs -> (int): количество ног у млекопитающего
    Методы:
        - lactate(): вырабатывать молоко
        - give_birth(): рожать потомство
    """

    def __init__(self, name, weight, speed, fur_type, habitat, number_of_legs):
        super().__init__(name, weight, speed)
        self.fur_type = fur_type
        self.habitat = habitat
        self.number_of_legs = number_of_legs

    def lactate(self):
        """
        Вырабатывать молоко.
        """
        pass

    def give_birth(self):
        """
        Рожать потомство.
        """
        pass

