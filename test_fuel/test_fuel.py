import pytest
from fuel import convert, gauge

def test_not_int():
      assert convert('2/4') == 50
      with pytest.raises(ValueError):
            convert('a/4')
      with pytest.raises(ValueError):
            convert('a/b')
      with pytest.raises(ValueError):
            convert('2/a')
def test_y_0():
      assert convert('2/4') == 50
      assert convert('0/5') == 0
      with pytest.raises(ZeroDivisionError):
           convert('2/0')
def test_x_greater():
      assert convert('3/4') == 75
      with pytest.raises(ValueError):
            convert('4/3')
def test_gauge():
      assert gauge(1) == 'E'
      assert gauge(0) == 'E'
      assert gauge(100) == 'F'
      assert gauge(99) == 'F'
      assert gauge(50) == '50%'
      assert gauge(33) == '33%'







