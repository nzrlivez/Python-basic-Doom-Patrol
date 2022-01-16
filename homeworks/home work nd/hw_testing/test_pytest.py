
import pytest
import functions_for_testing as test_func
import functions_pytest as fp


def test_season():
    assert fp.season('snow') == 'winter'
    assert fp.season('sun') == 'summer'
    assert fp.season('asdasdsa') is None


def test_range_list():
    assert 6 in fp.range_list(5, 10)
    assert 150 in fp.range_list(10, 200)
    assert 1500 in fp.range_list(10, 2000)


# homework10

def test_div():
    assert test_func.div(66, 6) == 11
    assert test_func.div(36, 6) == 6
