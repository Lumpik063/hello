from random import randint
so_many_times = input("Сколько шуток написать? ")

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num_of_jokes):
    jokes = []
    for i in range(num_of_jokes):
        jokes.append(nouns[randint(0, 4)] + " " + adverbs[randint(0, 4)] + " " + adjectives[randint(0, 4)])
    return jokes


print(get_jokes(int(so_many_times)))
