for number in list(range(1, 101)):
    if number <= 20:
        if number == 1:
            print(number, 'процент')
        elif 2 <= number <= 4:
            print(number, 'процента')
        else:
            print(number, 'процентов')
    else:
        last_digit = number % 10
        if last_digit == 1:
            print(number, 'процент')
        elif 2 <= last_digit <= 4:
            print(number, 'процента')
        else:
            print(number, 'процентов')
