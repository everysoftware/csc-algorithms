# O(N * W)
def knapsack_with_reps_bu(w, n, weight, cost):
    """
    C ПОВТОРЕНИЯМИ
    Рассмотрим оптимальное решение и предмет i в нём.
    Если вытащить данный предмет из рюкзака, то мы получим
    оптимальное заполнение рюкзака вместимости W - w_i (вырезать и вставить)
    Подзадачи:
    D[w] = макс. стоимость рюкзака вместимости w
    Тогда:
    D[w] = max_{i: w_i <= w}(D[w - w_i] + c_i)
    """
    d = [0] * (w + 1)
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            if weight[j - 1] <= i:
                d[i] = max(d[i], d[i - weight[j - 1]] + cost[j - 1])
    return d[w]