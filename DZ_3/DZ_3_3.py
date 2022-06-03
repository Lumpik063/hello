

def thesaurus(*args):
    many_names = {}

    for i in args:
        if i[0] in many_names:
            many_names[i[0]].append(i)

        else:
            many_names[i[0]] = [i]
    return many_names


put = thesaurus("Иван", "Мария", "Петр", "Илья")

print(put)

# Оператор распаковки (*args) конечно полезен, так как он позволяет вводить бесконечное колличество параметров.
# Словарь нельзя отсортировать, так как он не проиндексирован.