from typing import Callable

import pytest

from base_ds.application import sliding_window_naive, sliding_window_deque


@pytest.mark.parametrize("f", [sliding_window_naive, sliding_window_deque])
@pytest.mark.parametrize(
    "m, a, expected",
    [
        (3, [2, 1, 5, 3, 4, 6, 7], [5, 5, 5, 6, 7]),
        (4, [2, 1, 5, 3, 4, 6, 7], [5, 5, 6, 7]),
        (1, [2, 1, 5, 3, 4, 6, 7], [2, 1, 5, 3, 4, 6, 7]),
        (7, [2, 1, 5, 3, 4, 6, 7], [7]),
        (7, [7, 6, 5, 4, 3, 2, 1], [7]),
        (7, [1, 2, 3, 4, 5, 6, 7], [7]),
    ],
)
def test_sliding_window(
    f: Callable[[int, list[int]], list[int]], m: int, a: list[int], expected: list[int]
):
    assert f(m, a) == expected