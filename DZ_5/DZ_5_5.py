src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# 1. В этом способе на каждой итерации цикла, count обходит весь список, то есть, произходит очень много шагов. Это не есть хорошо)))

# unique_brands = [el for el in src if src.count(el) == 1]
# print(unique_brands)

# 2. В этом способе при итерации цикла проверяется, встречается ли текущий элемент ранее. Эта позволяет нам уменьшить количаство шагов. Хотя кода у нас больше, но по выполнению будет быстрее.

unique_brands = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
    tmp.add(el)

unique_brands_ord = [el for el in src if el in unique_brands]
print(unique_brands_ord)


