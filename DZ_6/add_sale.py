from sys import argv

with open('C:/test/study/bakery.csv', 'a') as file_1:
    file_1.write(argv[1]+'\n')

