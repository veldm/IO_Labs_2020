import module1
import module2
import module3
import module4
import module5
import module6

while True:
    print("""1) Числа и записи выражений
2) «Счастливый билет»
3) Операции со списками
4) Задача о Чебурашке
5) Калькулятор
6) Робот пишет по-русски
7)""")
    c = int(input("\nВведите номер задания: "))
    if c == 1:
        module1.Calculate()
    elif c == 2:
        module2.Check()
    elif c == 3:
        module3.Mas()
    elif c == 4:
        module4.Walk()
    elif c == 5:
        module5.Calculate()
    elif c == 6:
        module6.Write()
    else: print("Ошибка")
    print('\n')