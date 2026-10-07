from addition import add
from subtraction import subtract
from multiplication import multiply


def test_addition():
    assert add(10, 20) == 30


def test_subtraction():
    assert subtract(20, 10) == 10


def test_multiplication():
    assert multiply(10, 20) == 200