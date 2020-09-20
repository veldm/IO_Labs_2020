# Задание 4 - Задача о Чебурашке

def Walk():
    import numpy
    with open('Field.txt', 'r') as f:
        text = f.read().splitlines()
    #n = int(text[0])
    #m = int(text[1])
    #A = [[0] * m for i in range(n)]
    A = []
    for x in text:
        row = x.split()
        for i in range(len(row)):
            row[i] = int(row[i])
        A.append(row)
    for x in A:
        print(str(x))
    Results = []
    iter(A, 0, 0, 0, Results)
    Results.sort()
    print("Максимальная стоимость пути Чебурашки -", Results[len(Results) - 1])
     
def iter(Field, i, j, Sum, Results):
    Sum += Field[i][j]
    change = False
    if i < len(Field) - 1:
        iter(Field, i + 1, j, Sum, Results)
        change = True
    if j < len(Field[i]) - 1:
        iter(Field, i, j + 1, Sum, Results)
        change = True
    if not change:
        Results.append(Sum)
