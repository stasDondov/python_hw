class UkrIterator:
    """Ітератор для проходження символів рядка та
    знаходження українських"""

    def __init__(self, sen):  # sen - рядок, символи якого перевіряються
        self.k = len(sen)
        self._sen = sen
        self._index = -1
        self.alpha = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    def __iter__(self):
        """Метод __iter__ повертає сам об'єкт як ітератор."""
        return self

    def __next__(self):
        """Метод __next__ повертає наступний елемент послідовності у порядку слідування."""
        if self._index == self.k - 1:  # якщо дійшли до кінця послідовності
            raise StopIteration  # ініціювати виключення
        self._index += 1

        if self._sen[self._index] in self.alpha:
            return self._sen[self._index]


# Перевірка
sseq = 'lmknьрмоnjbпмор10иотл'
W = UkrIterator(sseq)
it = iter(W)
for i in it:
    if i != None:
        print(i)

