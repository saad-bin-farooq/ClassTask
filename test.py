from main import square, sub, sub_2

def test_square():
    assert 4 == square(2)
def test_sub():
    assert 1 == sub(4,3)
def test_sub2():
    assert 0 == sub_2(10)