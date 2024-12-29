import pytest

from controllers import operation


@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (5, -4, 1), (7, 8, 15), (-123, -456, -579), (12345, None, None), (None, -12345, None), (None, None, None)])
def test_operation(a: int | None, b: int | None, expected: int | None):
    received = operation(a, b)
    assert received == expected, f'Test for a={a}, b={b} falied: expected result is {expected}, received {received}'