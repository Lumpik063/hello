duration = [53, 153, 4153, 400153]

#Ответ на примечание: список полезен, сразу вводим все значения и получаем ответ.

for seconds in duration:
    if seconds < 60:
        print(seconds, 'сек')
    else:
        m = seconds // 60
        s = seconds % 60
        if m > 60:
            h = m // 60
            m = m % 60
            if h > 24:
                d = h // 24
                h = h % 24
                print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
            else:
                print(h, 'час', m, 'мин', s, 'сек')
        else:
            print(m, 'мин', s, 'сек')

