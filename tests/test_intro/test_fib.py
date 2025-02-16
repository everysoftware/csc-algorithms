from typing import Callable

import pytest

from src.a_intro import (
    fib_rec,
    fib_two_last,
    fib_mod_two_last,
    fib_mod_pisano,
    fib_bine,
)


@pytest.mark.parametrize("func", [fib_rec, fib_two_last, fib_bine])
@pytest.mark.parametrize(
    ["n", "expected"],
    zip([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 2, 3, 5, 8, 13, 21, 34]),
)
def test_fib(func: Callable[[int], int], n: int, expected: int):
    assert func(n) == expected


@pytest.mark.parametrize(
    "func",
    [
        fib_two_last,
    ],
)
@pytest.mark.parametrize(
    ["n", "expected"],
    zip(
        [10, 20, 30, 40, 100],
        [55, 6765, 832040, 102334155, 354224848179261915075],
    ),
)
def test_fib_huge(func: Callable[[int], int], n: int, expected: int):
    assert func(n) == expected


@pytest.mark.parametrize(
    "func",
    [
        fib_mod_two_last,
        fib_mod_pisano,
    ],
)
@pytest.mark.parametrize(
    ["n", "m", "expected"],
    [
        (10, 2, 1),
        (50, 13, 5),
    ],
)
def test_fib_mod(func: Callable[[int, int], int], n: int, m: int, expected: int):
    assert func(n, m) == expected


@pytest.mark.parametrize(
    "func",
    [
        fib_mod_pisano,
    ],
)
@pytest.mark.parametrize(
    ["n", "m", "expected"],
    [
        (60282445765134413, 2263, 974),
    ],
)
def test_fib_mod_huge(func: Callable[[int, int], int], n: int, m: int, expected: int):
    assert func(n, m) == expected
