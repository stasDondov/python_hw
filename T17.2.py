def corigator(f):
    """Декоратор @corigator для коригування результатів функції f"""

    def _corigator(x):
        a = -5  # a, b - деякі задані межі значень функції (a - min, b - max)
        b = 5
        if x < a:
            x = a
        elif x > b:
            x = b
        res = f(x)
        return res
    return _corigator


@corigator
def function(x):
    """Функція, що повертає число"""
    return x


# Перевірка
print(function(6))

