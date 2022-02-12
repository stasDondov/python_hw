from collections import defaultdict

n = int(input('Порядок матриці: '))  # задаємо матрицю
d = defaultdict(list)
print("Матриця:")  # елементи вводяться через пробіл
for i in range(n):
    S = enumerate(list(map(int, input().split())))
    for j in S:
        if j[1] != 0:
            d[(i, j[0])] = j[1]

Ans = max(d.values())

print('Найбільший елемент розрідженої матриці:', Ans)
print(d)

