numbers = list(range(1, 1001, 2))
final_sum = 0

for idx in range(len(numbers)):
    numbers[idx] = str(numbers[idx] ** 3)
for index in numbers:
    summa = 0
    for count in index:
        summa += int(count)
    if summa % 7 == 0:
        final_sum += int(index)
print(final_sum)


numbers_new = [((i ** 3) + 17) for i in range(1, 1001, 2)]
final_sum = 0

for index in numbers_new:
    summa = 0
    for count in str(index):
        summa += int(count)
    if summa % 7 == 0:
        final_sum += int(index)
print(final_sum)
