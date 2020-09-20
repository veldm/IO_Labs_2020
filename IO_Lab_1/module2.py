# Задание 2 - «Счастливый билет»

def Sum(a):
    sum = 0
    for x in a:
        sum += int(x)
    return sum

def Check():
    s = input("Введите номер билета: ")
    if len(s) % 2 == 1:
        print("Ошибка: номер билета должен иметь чётное число знаков")
    else:
        s1 = s[:((int)(len(s) / 2))]
        s2 = s[(int)(len(s) / 2):]
        import math
        dif = math.fabs(Sum(s1) - Sum(s2))
        if dif == 0:
            print("Билет счастливый")
        elif dif == 1:
            print("Билет встречный")
        else:
           print("Билет обычный")