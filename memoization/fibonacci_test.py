from memoization import fibonacci as f
import pytest

# Constants

FIB_5 = 5

FIB_100 = 354224848179261915075

FIB_1000 = '''
4346655768693745643568852767504062580
2564660517371780402481729089536555417
9490518904038798400792551692959225930
8032263477520968962323987332247116164
2996440906533187938298969649928516003
704476137795166849228875
'''

# Helper Methods

def large_num_to_s(s):
    return int(''.join([part.strip() for part in s.split('\n')]))

# Tests

def test_compute_5():
    assert f.compute(5) == FIB_5

def test_compute_100():
    assert f.compute(100) == FIB_100

def test_compute_1000():
    assert f.compute(1000) == int(large_num_to_s(FIB_1000))
