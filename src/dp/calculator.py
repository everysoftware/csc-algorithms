"""
https://stepik.org/lesson/13262/step/5?unit=3447

У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
заменить x на 2x, 3x или x+1. По данному целому числу 1 ≤ n ≤ 10^5 определите минимальное число операций k,
необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.
"""

INF = 10**20


def get_path(n: int, prev: list[int]) -> list[int]:
    """Восстановление пути. Сложность O(N)"""
    path = [n]

    while n > 1:
        n = prev[n]
        path.append(n)

    return path[::-1]


def calculator(n: int) -> list[int]:
    """Решение задачи о калькуляторе. Сложность O(N)"""
    min_ops = [INF] * (n + 1)
    """min_ops[i] - мин. число операций, чтобы получить из 1 число i"""
    prev = [-1] * (n + 1)
    """prev[i] - предыдущее число, из которого мы пришли в i"""
    min_ops[0] = 0
    min_ops[1] = 0

    for x in range(1, n + 1):
        moves = [x + 1, 2 * x, 3 * x]

        for i in moves:
            if i <= n and min_ops[x] + 1 < min_ops[i]:
                min_ops[i] = min_ops[x] + 1
                prev[i] = x

    return get_path(n, prev)