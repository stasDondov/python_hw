class ParametrError(Exception):
    """Помилка неправильної кількості параметрів"""

    def __str__(self):
        return '''Ви не ввели параметрів!'''


def function(*args, **kwargs):
    """Функція для обчислення"""

    if len(args) == 0:
        raise ParametrError

    assert len(args) == len(kwargs), 'Кількість позиційних та ключових параметрів неоднакова!'
    summ = 0
    kkeys = [j for j in kwargs.keys()]
    for i in kwargs.keys():
        summ += args[kkeys.index(i)] ** 2 + kwargs[i] ** 2 + args[kkeys.index(i)] * kwargs[i]
    return summ


# Перевірка
print(function(4, 1, 4, y1=5, y2=6))

