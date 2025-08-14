from working import convert
import pytest

def test_AM_PM():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('3 AM to 8 PM') == '03:00 to 20:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
def test_minutes():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('7:20 AM to 5:25 PM') == '07:20 to 17:25'
    assert convert('5:13 PM to 11:47 PM') == '17:13 to 23:47'
def test_AM_AM():
    assert convert('3 AM to 10 AM') == '03:00 to 10:00'
    assert convert('2:55 AM to 8:30 AM') == '02:55 to 08:30'
def test_PM_PM():
    assert convert('9 PM to 12 PM') == '21:00 to 12:00'
    assert convert('5 PM to 11 PM') == '17:00 to 23:00'
def test_PM_Am():
    assert convert('3 PM to 10 AM') == '15:00 to 10:00'
    assert convert('2:55 PM to 8:30 AM') == '14:55 to 08:30'




def test_error_meridiem():
    with pytest.raises(ValueError):
        convert('3 to 10 ')

def test_errors_minutes():
    with pytest.raises(ValueError):
        convert('3:77 AM to 10:13 PM ')

def test_errors_to():
    with pytest.raises(ValueError):
        convert('3:00 AM - 10:00 PM ')


def test_errors_over():
    with pytest.raises(ValueError):
        convert('3:00 AM to 25:00 PM')
    with pytest.raises(ValueError):
        convert('55:00 AM to 1:00 PM')
