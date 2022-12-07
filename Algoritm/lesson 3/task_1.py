'''Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!"""
import time
'''

def timer_wrapper(func):
    def timer(args, kwargs):
        star_timer = time.perf_counter()
        func(args, kwargs)
        stop_timer = time.perf_counter()
        return print(func.__name__, stop_timer - star_timer)
    return timer


''' add_list - заполняет список '''
@timer_wrapper
def add_list(mylist, nums):
    for i in range(nums):
        mylist.append(i)   #O(1)
    return mylist


my_list = []
num = 3**10
add_list(my_list, num)


''' add_dict - заполняет словарь '''
@timer_wrapper
def add_dict(mydict, nums):
    for i in range(nums):
        mydict[i] = True      #O(1)
    return mydict


my_dict = {}
num = 3**10
add_dict(my_dict, num)


'''take_elem_list - получает значения из списка'''
@timer_wrapper
def take_elem_list(mylist, num):
    for i in range(num):
        return mylist[i] #0(1)


nums2 = 2000
take_elem_list(my_list, nums2)


'''take_elem_dict - получает значения из словаря'''
@timer_wrapper
def take_elem_dict(mydict, num):
    for i in range(num):
        return mydict.get(i) #O(1)


nums2 = 2000
take_elem_dict(my_dict, nums2)

'''del_elem_list - удаляет элементы из списка'''
@timer_wrapper
def del_elem_list(mylist, num):
    for i in range(num):
        mylist.pop(i)  #O(1)
    return mylist


num3 = 10000
del_elem_list(my_list, num3)


'''del_elem_dict - удаляет элементы из словаря'''
@timer_wrapper
def del_elem_dict(mydict, num):
    for i in range(num):
        mydict.pop(i)  #O(1)
    return mydict


num3 = 10000
del_elem_dict(my_dict, num3)

'''Вывод:
Заполнение словаря занимает больше времени из-за того, что ему неоходимо хешировать данные.
add_list 0.008433319046162069
add_dict 0.012216356000863016
Получение значение у словаря тоже занимает меньше времени, потому что сравниваются хеши ключей, 
а списки перебираются
take_elem_list 1.1290016118437052e-05
take_elem_dict 1.0775984264910221e-05
Тут я не знаю почему такия разница.
Удаление списка намного медленее потому что...(и тут преподаватель объясняет)
del_elem_list 0.23062668996863067
del_elem_dict 0.0015020280261524022'''