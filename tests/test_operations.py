from py_fao.operations import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(4, 2) == 2


def test_multiply():
    assert multiply(3, 3) == 9


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(1, 0)
