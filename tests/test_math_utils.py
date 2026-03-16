from math_utils import mul, sum


def test_sum_positive_numbers():
    assert sum(2, 3) == 5


def test_sum_negative_numbers():
    assert sum(-1, -2) == -3


def test_mul_basic():
    assert mul(2, 3) == 6
