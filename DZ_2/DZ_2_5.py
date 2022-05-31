price = [57.8, 46.51, 97, 105.5, 44.3, 20, 168.33, 65.7, 111.1, 65, 23.4, 91.8]

#1
str_price = []
for correct in price:
    result = str(correct).split('.')
    if len(result) == 1:
        result.append('00')
    str_price.append(result)

    if len(result[1]) == 1:
        result[1] += '0'

count = 0
end = ', '
for rub, kop in str_price:
    count += 1
    if len(str_price) == count:
        end = '\n'
    print(rub, 'руб', kop, 'коп', end=end)

#2
address = []
address_max = []

for i in price:
    address.append(id(i))

price.sort()
print(price)

#3
for i in price:
    address_max.append(id(i))

result = [x for x in address + address_max if x not in address or x not in address_max]
if not result:
    print('Объекты списка после сортировки остались те же.')
else:
    print('Объекты списка после сортировки стали разные.')

#4
price_min = price.copy()
price_min.sort(reverse=True)
print(price_min)

#5
print(price_min[:5])
