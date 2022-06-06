numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(number):
    if number in numbers:
        return numbers[number]
    else:
        return 'None'


number = input("Напишите число, которое нужно перевести: ")
print(num_translate(number))

#Тип данных - это словарь. А хранить лучше снаружи тела функции. Чтобы при вызове функции, обращение отправлялось в существующую ячейку со славарем, а не каждый раз создавала новую.
