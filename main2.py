#НАВАСАРДЯН 25ИСИП9-1
#1,2
def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)
# Этот вызов сработает без ошибок в любом случае
lets_go('Гарри', 'ловить Волан-де-Морта')
# Вызов без аргументов, сработает благодаря значениям по умолчанию
lets_go()
#3
def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)
# Исправленный вызов: передаём аргумент в параметр target по имени
lets_go(target='читать следующий урок!')
#4
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
for n in range(20, 32):
    print(n, factorial(n))
#5
def count_digits(n: int) -> int:
    return len(str(abs(n)))
#6
def sum_to_n_loop(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
#7
def power(base: float, exponent: int) -> float:
    result = 1
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    for _ in range(exponent):
        result *= base
    return result
#8
def print_divisors(n: int):
    if n <= 0:
        print("Введите положительное число.")
        return
    divisors = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisors.append(d)
    print(divisors)