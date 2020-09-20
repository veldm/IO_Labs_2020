# Решение квадратных уравнений
import math

def Solve():
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
    except Error as E:
        print("Некорерктный ввод")

    res =""
    res += (str(a) + "x^2")
    if b > 0: res += (" + " + str(b) + "x")
    elif b < 0: res += (" - " + str((int)(math.fabs(b))) + "x")
    if not c == 0: res += (" + " + str(c))
    res += " = 0"
    print("На вход получено уравнение ", res)
    if (a == 0 and b == 0 and c == 0):
        pass
    elif (a == 0 and b == 0):
        print("Ошибка - вместо уравнения введено неправильное равенство")
    elif ((a == 0 and c == 0) or (b == 0 and c ==0)):
        print("x = 0")
    elif a == 0: print("x = ", c / b)
    elif b == 0:
        p = -1 * (c / a)
        if p >=0: print("x1 =", math.sqrt(p), "  x2 =", -1 * math.sqrt(p))
        else: print("Уравнение не имеет корней")
    elif c == 0:
        print("x1 = 0   x2 = ", -1 * (b / a))
    else:
        if ((b ** 2) - (4 * a * c) < 0):
            print("Уравнение не имеет корней")
        else:
            x1 = (-b + ((b ** 2) - (4 * a * c))) / (2 * a)
            x2 = (-b - ((b ** 2) - (4 * a * c))) / (2 * a)
            print("x1 =", x1, "  x2 =", x2)
