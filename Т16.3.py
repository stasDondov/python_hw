class SeqIterator:
    """Ітератор для проходження елементів послідовності seq"""

    def __init__(self, seq, var):
        """Для повернення елементів з парними індексами: var = 'even'
        для повернення елементів з непарними індексами: var = 'odd' """

        self.k = len(seq)
        self._seq = seq  # odd - непарний
        self._index = -1  # even - парний
        self._var = var

    def __iter__(self):
        """Метод __iter__ повертає сам об'єкт як ітератор."""
        return self

    def __next__(self):
        """Метод __next__ повертає наступний елемент послідовності у порядку слідування."""
        if self._index == self.k - 1:  # якщо дійшли до кінця послідовності
            raise StopIteration  # ініціювати виключення
        self._index += 1

        if self._var == 'even' and self._index % 2 == 1:
            return self._seq[self._index]

        elif self._var == 'odd' and self._index % 2 == 0:
            return self._seq[self._index]


# Перевірка
sseq = [1, 4, 5, 7, 1, 9, 2, 6, 10]
W = SeqIterator(sseq, 'odd')
it = iter(W)
for i in it:
    if i != None:
        print(i)

