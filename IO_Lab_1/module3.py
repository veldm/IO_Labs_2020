# Операции со списками

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