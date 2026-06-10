import pytest

@pytest.mark.order(1)
def test_Sample1():
    assert 1 + 1 == 2
    print("Test 1 passed")

@pytest.mark.order(2)
def test_Sample2():
    assert 1 + 1 == 2
    print("Test 2 passed")

@pytest.mark.order(3)
def test_Sample3():
    assert 1 + 1 == 2
    print("Test 3 passed")