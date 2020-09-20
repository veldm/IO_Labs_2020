# Задание 6 - Робот пишет по-русски

def Write():
    W = int(input("Введите число: "))
    V = W % 10
    if (V == 0 or V > 4):
        print(W, "программистов")
    elif (V == 1):
        print(W, "программист")
    elif (V > 1 and V < 5):
        print(W, "программиста")
