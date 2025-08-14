from plates import is_valid

def test_start_2L():
    assert(is_valid("CS50")) == True
    assert(is_valid("C293")) == False
    assert(is_valid("50CS")) == False
    assert(is_valid("5CSF")) == False



def test_range_char():
    assert(is_valid("ABC")) == True
    assert(is_valid("A")) == False
    assert(is_valid("ABCDEFG")) == False

def test_contain_char():
    assert(is_valid("CS50")) == True
    assert(is_valid("C.S50")) == False
    assert(is_valid("CS50,")) == False
    assert(is_valid("CS 50")) == False

def test_start_0():
    assert(is_valid("CS50")) == True
    assert(is_valid("CS05")) == False

def test_num_loc():
    assert(is_valid("AAA22A")) == False
    assert(is_valid("AAA22")) == True
