from jar import Jar
import pytest


def test_set_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.set_capacity(-1)

def test_set():
    jar = Jar()
    jar.set_capacity(2)
    assert jar.get_capacity() == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit_error():
    jar = Jar()
    assert jar.get_size() == 0
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_deposit():
    jar = Jar()
    assert jar.get_size() == 0
    jar.deposit(5)
    assert jar.get_size() == 5



def test_withdraw_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.get_size() == 3
    jar.withdraw(2)
    assert jar.get_size() == 1

