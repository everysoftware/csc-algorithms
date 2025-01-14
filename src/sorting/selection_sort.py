# O(N^2)
def selection_sort(a: list[int]) -> None:
    """
    Принцип работы: находим минимум, ставим его первым,
    находим 2-й минимум, ставим его вторым и т. д.
    """
    n = len(a)
    for i in range(n):
        # Ищем минимум в оставшейся части массива
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
