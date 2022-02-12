def Viraz(matr, var):
    """Для повернення індексів найменших елементів: var = 'min'
    для повернення індексів найбільших елементів: var = 'max' """

    n = len(matr)  # n - к-кість рядків заданої матриці
    m = len(matr[0])  # m - к-кість стовпців заданої матриці
    Ans = [[matr[i][j], (i, j)] for j in range(m) for i in range(n)]  # Ans - генератор-вираз
    print('Елементи матриці разом з індексами:')
    for i in Ans:
        print(i[0], ':', i[1])

    if var == 'min':  # a)
        Minimal = min([i[0] for i in Ans])  # Minimal - найменше значення елементу матриці
        print('\nНайменший елемент:', Minimal, '\n')
        print('Координати елементів рівних найменшому:')
        Str = ''
        for i in Ans:
            if i[0] == Minimal:
                Str += str(i[1]) + '\n'
        return Str

    if var == 'max':  # b)
        Maximal = max([i[0] for i in Ans])  # Maximal - найбільше значення елементу матриці
        print('Найбільший елемент:', Maximal, '\n')
        print('Координати елементів рівних найбільшому:')
        Str = ''
        for i in Ans:
            if i[0] == Maximal:
                Str += str(i[1]) + '\n'
        return Str


# Перевірка
matr = [[1, 1, -1], [-1, -1, 1]]
print(Viraz(matr, 'max'))

