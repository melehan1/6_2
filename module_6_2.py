from colorama import Fore, Back, Style


class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.__COLOR_VARIANTS = ['green', 'red', 'yellow', 'blue', 'teal', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}')
        print(f'{self.get_horsepower()}')
        print(f'{self.get_color()}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.upper() not in self.__COLOR_VARIANTS and new_color.lower() not in self.__COLOR_VARIANTS:
            print(Fore.YELLOW + f'Невозможно покрасить в {new_color}'+ Style.RESET_ALL)
        if new_color.upper() in self.__COLOR_VARIANTS or new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color


class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)
        self.__PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
