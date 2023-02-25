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

    def say(self, sound):
        """
        Это внутренний метод для произношения звука животным.
        """
        print(f"{self.name} издает звук {sound}.")

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
        - wingspan -> (float): размах крыльев в метрах
        - flight_altitude -> (float): максимальная высота полета в метрах
    Методы:
        - lay_eggs(): птица несет яйца
        - build_nest(): птица строит гнездо для откладывания яиц
    """
    def __init__(self, name, weight, speed, wingspan, flight_altitude):
        super().__init__(name, weight, speed)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def build_nest(self):
        """
        Птица строит гнездо для откладывания яиц.
        """
        print(f"{self.name} строит гнездо для откладывания яиц.")

    def lay_eggs(self):
        """
        Нести яйца.
        """
        pass

class Eagle(Birds):
    """
    Подкласс класса Birds, который описывает орлов.
    Атрибуты:
        - eyesight -> (float): острота зрения орла
        - prey -> (str): добыча, которую охотится орел
    Методы:
        - hunt(): охотиться на добычу
    """
    def __init__(self, name, weight, speed, wingspan, flight_altitude, eyesight, prey):
        super().__init__(name, weight, speed, wingspan, flight_altitude)
        self.eyesight = eyesight
        self.__prey = prey

    @property
    def prey(self):
        return self.__prey

    @prey.setter
    def prey(self, new_hunted_prey):
        if new_hunted_prey < 0:
            print("Количество добычи не может быть отрицательным")
        else:
            self.__prey = new_hunted_prey

    def hunt(self):
        """
        Охотиться на добычу.
        """
        print(f"{self.name} охотится на {self.prey}.")

class Penguin(Birds):
    """
    Подкласс класса Birds, который описывает пингвинов.
    Атрибуты:
        - flight_altitude -> (float): максимальная высота полета в метрах (для пингвина по умолчанию = 0)
    Методы:
        - swim(): пингвин плавает в воде
    """
    def __init__(self, name, weight, speed, wingspan, flight_altitude=0):
        super().__init__(name, weight, speed, wingspan, flight_altitude)

    def swim(self):
        """
        Пингвин плавает в воде.
        """
        print(f"{self.name} плавает.")

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


class Snake(Reptile):
    """
    Подкласс, описывающий змей.
    Атрибуты наследованные от родителя:
        - name -> (str): имя змеи
        - weight -> (float): вес змеи в кг
        - speed -> (float): скорость змеи в км/ч
        - is_poisonous -> (bool): флаг, является ли змея ядовитой
        Собственный атрибут:
        - length -> (float): длина змеи в метрах
    """
    def __init__(self, name, weight, speed, length, is_poisonous):
        super().__init__(name, weight, speed, is_poisonous)
        self.length = length


class Lizard(Reptile):
    """
        Подкласс, описывающий ящериц.
        Атрибуты наследованные от родителя:
            - name -> (str): имя ящерицы
            - weight -> (float): вес ящерицы в кг
            - speed -> (float): скорость ящерицы в км/ч
            - is_poisonous -> (bool): флаг, является ли ящерица ядовитой
            Собственный атрибут:
            - age -> (int): возраст ящерицы в годах
        """
    def __init__(self, name, weight, speed, age, is_poisonous):
        super().__init__(name, weight, speed, is_poisonous)
        self.age = age

class Mammals(Animal):
    """
    Подкласс класса Animal, описывающий млекопитающих.
    Атрибуты:
        - habitat -> (str): место обитания млекопитающего
        - number_of_legs -> (int): количество ног у млекопитающего
    Методы:
        - lactate(): вырабатывать молоко
        - give_birth(): рожать потомство
    """

    def __init__(self, name, weight, speed, habitat, number_of_legs):
        super().__init__(name, weight, speed)
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
class Carnivore(Mammals):

    """
    Подкласс класса Mammals, описывающий плотоядных млекопитающих.
        Атрибуты:
        - prey -> (str): добыча
    Методы:
        - hunt(): охотиться на добычу
    """

    def __init__(self, name, weight, speed, habitat, number_of_legs, prey):
        super().__init__(name, weight, speed, habitat, number_of_legs)
        self.prey = prey

    def hunt(self):
        """
        Охотиться на добычу.
        """
    pass

class Herbivore(Mammals):

    """
    Подкласс класса Mammals, описывающий травоядных млекопитающих.
        Атрибуты:
        - diet -> (str): рацион
    Методы:
        - graze(): пастись
    """

    def __init__(self, name, weight, speed, habitat, number_of_legs, diet):
        super().__init__(name, weight, speed, habitat, number_of_legs)
        self.diet = diet

    def graze(self):
        """
        Пастись.
        """
    pass
