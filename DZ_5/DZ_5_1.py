import time


def gen_range(stop_value, current=1, step=2):
    while current <= stop_value:
        yield current
        current += step


odd_to = gen_range(7)

while True:
    print(next(odd_to))

