

def gen_new_list(tutors, klasses):
    i = 0
    while i < len(tutors) and i < len(klasses):
        yield tutors[i], klasses[i]
        i += 1
    while i < len(tutors):
        yield tutors[i], None
        i += 1


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Алексей', 'Оксана']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

print(type(gen_new_list(tutors, klasses))) #Доказываем, что это генератор.

final_result = gen_new_list(tutors, klasses)
while True:
    print(next(final_result))


