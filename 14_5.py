from collections import defaultdict

n = int(input('Порядок матриці: '))   #задаємо матрицю
Matr = []
for i in range(n):
    S = list(map(int, input().split()))
    Matr.append(S)


d = defaultdict(list)
for i in range(len(Matr)):
    for j in range(i):
        d[(i, j)] = Matr[i][j]

print(d[(0, 0)])

