from typing import Any
from typing import Callable

"""
Should return last index of "true"
left: <   right: <=
[1, 2, 3, 4, 5, 6, 7, 8] , 3
 T  T F/T F  F  F  F  F
so left -> 1, right -> 2
"""


def b_left(arr: list[Any], val: Any) -> int:
    """
    [1,  2,  3,  4,  5, 6, 7, 8], 3
     1   2   3  !<4
     1   2<
         return index 2
    """
    return _bisect_search(arr, val, lambda a, b: a < b)


def b_right(arr: list[Any], val: Any) -> int:
    return _bisect_search(arr, val, lambda a, b: a <= b)


def _bisect_search(
    arr: list[Any],
    val: Any,
    # python quirk: comparison returns Any, not bool
    comparison: Callable[[Any, Any], Any],
    lo: int = 0,
    hi: int = -1,
) -> int:
    if hi < 0:
        hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if comparison(arr[mid], val):
            lo = mid + 1
        else:
            hi = mid
    return hi
