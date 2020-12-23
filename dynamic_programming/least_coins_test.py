from dynamic_programming import least_coins as lc
import pytest

def test_compute_scenario1():
    available_coins = [1, 3, 5]

    result = lc.compute(11, available_coins)
    
    assert result != []
    assert sum(result) == 11
    assert sorted(result) == [1, 5, 5]
    
def test_compute_scenario2():
    available_coins = [50, 100]

    result = lc.compute(75, available_coins)
    
    assert result is None

def test_compute_scenario3():
    available_coins = [1, 3, 5, 8]

    result = lc.compute(16, available_coins)
    
    assert result != []
    assert sum(result) == 16
    assert sorted(result) == [8, 8]

def test_compute_scenario4():
    available_coins = [1, 3, 5, 8]

    result = lc.compute(35, available_coins)
    
    assert result != []
    assert sum(result) == 35
    assert sorted(result) == [3, 8, 8, 8, 8]

def test_compute_scenario5():
    available_coins = [6, 8, 10]

    result = lc.compute(35, available_coins)
    
    assert result is None
