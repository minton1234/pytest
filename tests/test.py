import product

# def test_one():

#     fizbaz = product.Fizbaz()
#     expected = fizbaz.convert(1)
#     assert "1" == expected

# def test_two():

#     fizbaz = product.Fizbaz()
#     expected = fizbaz.convert(2)
#     assert "2" == expected

# def test_three():

#     fizbaz = product.Fizbaz()
#     expected = fizbaz.convert(3)
#     assert "Fiz" == expected
import pytest

@pytest.fixture
def db():
    fizbaz = product.Fizbaz()
    return fizbaz

def test_fizbaz(db, number=3):
    expected = db.convert(number)
    assert "Fiz" == expected

def test_fizbaz(db, number=5):
    expected = db.convert(number)
    assert "baz" == expected


