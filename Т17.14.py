def modificator(f):
    """Декоратор @modificator для модифікації списку"""

    def _modificator(**kwargs):
        ans = []  # ans - 'очищений' список
        res = f(**kwargs)
        for i in res:
            if i not in ans:
                ans.append(i)
        return ans

    return _modificator


@modificator
def spisok(fname='File.txt'):
    """Функція, що створює список зі слів файла fname"""
    List = []
    F = open(fname, 'r+')
    W = F.readlines()
    for i in W:
        i = i.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
        line = i.lower().split()
        for j in line:
            if j != '':
                List.append(j)
    return List


# Перевірка
print(spisok())

