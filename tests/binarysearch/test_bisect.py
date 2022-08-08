from bisect import bisect_left
from bisect import bisect_right
from typing import Any

import pytest
from binarysearch.bisect_search import b_left
from binarysearch.bisect_search import b_right


@pytest.mark.xfail
def test_expected_fail() -> None:
    assert 1 == 1.0


@pytest.mark.xfail
def test_surprise_works() -> None:
    assert 1 == 1


def test_basic() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert b_left(arr, 3) == 2
    assert b_right(arr, 3) == 3


@pytest.mark.parametrize(
    "array,value",
    [
        ([], 1),
        ([1, 1, 1], 1),
        ([1, 1, 1], 5),
        ([1, 1, 1, 7, 7, 7], 5),
        ([1, 1, 1, 7, 7, 7], 1),
        ([1, 1, 1, 7, 7, 7], 7),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 0),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 1),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 3),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 8),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 12),
    ],
)
def test_param_compare_with_builtin(array: list[Any], value: Any) -> None:
    assert bisect_left(array, value) == b_left(array, value)
    assert bisect_right(array, value) == b_right(array, value)
