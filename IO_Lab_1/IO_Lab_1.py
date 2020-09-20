import module1
import module2



while True:
    print("""1) Числа и записи выражений
2) «Счастливый билет»
3)
4)
5)
6)
7)""")
    c = int(input("\nВведите номер задания: "))
    if c == 1:
        module1.Calculate()
    elif c == 2:
        module2.Check()
    
    else: print("Ошибка")
    print('\n')