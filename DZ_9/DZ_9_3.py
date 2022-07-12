class Worker:

    __income = {
        'wage': 20000,
        'bonus%': 150
    }

    def __init__(self, name, surname, position):

        self.name = name
        self.surname = surname
        self.position = position
        self.income = self.__income


class Position(Worker):


    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        print(f"месячная заработная плата составляет: {self.income['wage']}$ + премия {self.income['wage']//100*150}$")


if __name__ == '__main__':
    Natali = Position('Наталья', 'Иванова', 'Начальник отдела')
    Natali.get_full_name()
    Natali.get_total_income()
    print(f'{Natali.name} is {Natali.position}')