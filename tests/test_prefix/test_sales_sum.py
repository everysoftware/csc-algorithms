import pytest

from prefix.implementation import sales_sum


@pytest.mark.parametrize("sales, queries, expected", [
    # Тест 1: Проверка на примере
    ([100, 200, 300, 400, 500], [(0, 2), (1, 3), (0, 4)], [600, 900, 1500]),
    # Тест 2: Проверка на массиве с одним элементом
    ([100], [(0, 0)], [100]),
    # Тест 3: Проверка на массиве с двумя элементами
    ([100, 200], [(0, 1)], [300]),
    ([100, 200], [(0, 0), (1, 1)], [100, 200]),
    # Тест 4: Проверка на массиве с несколькими элементами
    ([100, 200, 300, 400, 500], [(0, 4)], [1500]),
    ([100, 200, 300, 400, 500], [(0, 2), (1, 3), (2, 4)], [600, 900, 1200]),
])
def test_sales_sum(sales: list[int], queries: list[tuple[int, int]], expected: list[int]):
    assert sales_sum(sales, queries) == expected