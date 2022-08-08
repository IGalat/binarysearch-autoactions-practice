from typing import Any
from typing import Callable
from typing import Iterable


def b_left(arr: Iterable[Any], val: Any) -> int:
    pass


def b_right(arr: Iterable[Any], val: Any) -> int:
    pass


def _bisect(
    arr: Iterable[Any], val: Any, comparison: Callable[[Any, Any], bool]
) -> int:
    pass
