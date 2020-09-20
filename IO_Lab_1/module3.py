# Задание 3 - Операции со списками

def Mas():
    N = int(input("Введите размер массива: "))
    A = []
    for i in range(N):
        A.append(int(input("Введите число {0} из {1}: ".format(i + 1, N))))

    list.sort(A);
    Max = A[N - 1]
    print("Максимальное число в массиве -", Max)
    Min = A[0]
    print("Минимальное число в массиве -", Min)
    Sum = 0
    for x in A: Sum += x
    print("Сумма элементов массива -", Sum)    

    # ------------------------------

    print("\nГенерирую новый массив...")
    input()
    B = []
    from random import randint
    N = randint(10, 35)
    for i in range(N):
       B.append(randint(1, 99))
    print("Новый массив:\n", str(B))

    list.sort(B);
    Max = B[N - 1]
    print("Максимальное число в массиве -", Max)
    Min = B[0]
    print("Минимальное число в массиве -", Min)
    Sum = 0
    for x in B: Sum += x
    print("Сумма элементов массива -", Sum)    

    # ------------------------------

    print("\nСоздание массива с помощью библиотеки numpy...")
    input()
    import numpy
    N = randint(5, 15)
    C = numpy.zeros(N)
    print("\nnumpy.zeros({0})\n".format(N), str(C))

    a = randint(0, 10)
    b = randint(35, 50)
    c = randint(1, 5)
    D = numpy.arange(a, b, c)
    print("\nnumpy.arange({0}, {1}, {2})\n".format(a, b, c), str(D))

    E = numpy.array(B, int)
    print("\nnumpy.array(B, int)\n", str(E))