numbers = int(input())
odd_to = (i for i in range(numbers + 1) if i % 2 != 0)
while True:
    print(next(odd_to))