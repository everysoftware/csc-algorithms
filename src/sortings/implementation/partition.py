"""Разбиение массива на части"""


def partition2(a: list[int], left: int | None = None, right: int | None = None) -> int:
    """
    Разбиение массива на две части: меньшие опорного и большие опорного. В качестве опорного берётся первый элемент.
    Возвращает индекс опорного элемента. Сложность O(N).
    """
    left = left if left is not None else 0
    right = right if right is not None else len(a) - 1
    pivot = a[left]

    j = left
    """j - индекс опорного элемента"""

    # проходим по всем элементам массива
    for i in range(left + 1, right + 1):
        # если текущий элемент меньше опорного, меняем их местами
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    a[left], a[j] = a[j], a[left]

    return j


def partition3(
    a: list[int], left: int | None = None, right: int | None = None
) -> tuple[int, int]:
    """
    Разбиение массива на три части: меньшие опорного, равные опорному и большие опорного.
    В качестве опорного берётся первый элемент.
    Возвращает индексы начала и конца равных опорному элементу. Сложность O(N).
    """
    left = left if left is not None else 0
    right = right if right is not None else len(a) - 1
    pivot = a[left]

    i = left + 1
    while i <= right:
        # если текущий элемент меньше опорного, меняем их местами
        if a[i] < pivot:
            a[i], a[left] = a[left], a[i]
            left += 1
            i += 1

        # если текущий элемент больше опорного, меняем его с правым элементом
        elif a[i] > pivot:
            a[i], a[right] = a[right], a[i]
            right -= 1

        # если текущий элемент равен опорному, просто переходим к следующему элементу
        else:
            i += 1

    return left, right