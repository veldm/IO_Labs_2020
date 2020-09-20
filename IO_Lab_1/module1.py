#Задание 1 - Числа и записи выражений

def Calculate():
    # Простое выражение
    print("Вычисление простого выражения:")
    a = (1 / 3) * 0.99 + 2
    s = "1/3 * 0.99 + 2 = {0}".format(a)
    print(s)
    # Сложное выражение
    print("Вычисление сложного выражения:")
    import math
    a1 = math.pow(2, 5) * (math.sin(12.3) + math.cos(52.7 * (31 / math.pow(73, 2.5)))
                           * (math.sin(12.3) + math.cos(52.7 * (31 / math.pow(73, 2.5)))))
    a2_0 = 12.3 + 52.7 * (31 / math.pow(73, 2.5))
    a2_1 = math.log(math.pow(a2_0, (1 / 3)))
    a2_2 = 0.233 * (math.pow(10, 4) / math.pow(2, 7))
    a2 = a2_1 - a2_2
    a = (a1 / a2)
    print("Результат: " + str(a))