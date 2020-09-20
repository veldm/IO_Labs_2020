# Задание 5 - Калькулятор

def Calculate():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Поддерживаемые операции: +, -, /, *, mod, pow, div.")
    operation = input("Введите обозначение операции: ")
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "/":
        if not b == 0:
            print(a / b)
        else:
            print("На 0 делить нельзя!")
    elif operation == "*":
        print(a * b)
    elif operation == "mod":
        print(a % b)
    elif operation == "pow":
        print(a ** b)
    elif operation == "div":
        print(a // b)
    else:
        print("Операция \"%s\" не поддерживается в калькуляторе" % (operation))
