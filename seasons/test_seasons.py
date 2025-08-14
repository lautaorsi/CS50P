import pytest
from datetime import date
import datetime
from seasons import word
from seasons import forma

import inflect


def test_format():
    with pytest.raises(SystemExit):
      forma('January')
    with pytest.raises(SystemExit):
      forma('1999/01/01')
    assert forma('2003-02-25') == datetime.datetime.strptime('2003-02-25 00:00:00', "%Y-%m-%d %H:%M:%S").date()
    assert forma('1995-12-25') == datetime.datetime.strptime('1995-12-25 00:00:00', "%Y-%m-%d %H:%M:%S").date()

def test_words():
    p = inflect.engine()
    assert word(52700) == p.number_to_words(52700, andword=" ")
    assert word(45) == p.number_to_words(45, andword=" ")
    assert word(1252700) == p.number_to_words(1252700, andword=" ")


