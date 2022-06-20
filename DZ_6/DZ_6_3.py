import sys

with open('C:/test/study/users.csv', 'r') as file_1:
    users = file_1.readlines()

with open('C:/test/study/hobby.csv', 'r') as file_2:
    hobby = file_2.readlines()


into_one = {}

if len(users)>len(hobby):
    for i in range(len(users)):
        if i < len(hobby):
            into_one[users[i]] = hobby[i]
        else:
            into_one[users[i]] = None

    print(into_one)

else:
    for i in range(len(hobby)):
        if i < len(users):
            into_one[users[i]] = hobby[i]
        else:
            print(into_one)
            sys.exit(1)
