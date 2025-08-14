from um import count
import pytest

def test_mum():
    assert count('mum') == 0
    assert count('clumsy') == 0
    assert count('um') == 1
    assert count('umn') == 0

def test_um_space():
    assert count(' um') == 1
    assert count('um ') == 1
    assert count(' um ') == 1
    assert count('  um') == 1
    assert count('um  ') == 1
    assert count('  um  ') == 1
def test_um_punc():
    assert count('um.') == 1
    assert count('um,') == 1
    assert count('um?') == 1
    assert count('um.,.,') == 1
    assert count('um,?') == 1
    assert count('um_') == 0
def test_um_caseins():
    assert count('UM') == 1
    assert count('um') == 1
    assert count('Um') == 1
    assert count('uM') == 1
