from bank import value




def test_start_h():
    assert(value("hey")) == 20




def test_start_hello():
    assert(value("Hello")) == 0
    assert(value("hello, newman")) == 0



def test_start_else():
    assert(value("wassup")) == 100


