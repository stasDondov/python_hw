from functools import wraps

def trace(debug):
    """Декоратор @trace для відсліковування виконання функції f.
    Параметр debug вказує, чи здійснювати трасування"""

    def _trace(f):
        count = 0  # count - лічильник рекурсивних викликів

        @wraps(f)  # декоратор оновлює значення атрибутів __trace відповідними атрибутами f
        def __trace(var):  # var - параметр функції f
            nonlocal count
            count += 1

            if debug:
                print('\nВхід до', f.__name__, )
                print('Номер рекурсивного виклику:', count)
                print('Параметр перед викликом: n =', var)
            res = f(var)  # викликаємо f

            if debug:
                print('\nВихід з', f.__name__)
                print('Параметр після виклику: n =', res)
            return res

        return __trace

    return _trace


@trace(True)
def factorial(n):
    """Функція для знаходження факторіалу числа n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@trace(True)
def fibonacci(n):
    """Функція для знаходження n-го числа Фібоначчі"""
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Перевірка
A = factorial(3)
print('\nФакторіал: ', A, '\n')

B = fibonacci(3)
print('\nЧисло Фібоначчі:', B)

