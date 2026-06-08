import pytest

@pytest.mark.smoke
def test_Sample1():
    assert 1+1 == 2
    print("Test 1 passed")

@pytest.mark.regression
def test_Sample2():
    assert 1+1 == 2
    print("Test 2 passed")

@pytest.mark.xfail(reason="No need")
def test_Sample3():
    assert 1+1 == 3
    print("Test 3 passed")



