import pytest
from binarysearch.bisect import b_left


@pytest.mark.xfail
def test_b_left() -> None:
    assert b_left([1, 2, 3], 2) == 1
