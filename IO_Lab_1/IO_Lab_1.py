import module1
import module2
import module3
import module4

while True:
    print("""1) Числа и записи выражений
2) «Счастливый билет»
3) Операции со списками
4) Задача о Чебурашке
5)
6)
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
    else: print("Ошибка")
    print('\n')