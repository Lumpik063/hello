from sys import argv

with open('C:/test/study/bakery.csv', 'r') as file_1:
    prices = file_1.readlines()
if len(argv) == 1:
    print(prices)
elif len(argv) == 2:
    print(prices[int(argv[1]):])
else:
    print(prices[int(argv[1]): int(argv[2])])
