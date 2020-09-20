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

