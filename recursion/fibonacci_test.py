from recursion import fibonacci as f
import pytest

FIB_5 = 5
FIB_10 = 55
FIB_25 = 75025


def test_compute_5():
    assert f.compute(5) == FIB_5


def test_compute_10():
    assert f.compute(10) == FIB_10


def test_compute_25():
    assert f.compute(25) == FIB_25
