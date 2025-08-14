from numb3rs import validate

def test_fst():
    assert(validate('0.3.25.25')) == True
    assert(validate('255.5.25.27')) == True
    assert(validate('-1.25.25.25')) == False
    assert(validate('300.25.25.25')) == False
    assert(validate('300.25.25.25.25')) == False

def test_snd():
    assert(validate('25.0.99.25')) == True
    assert(validate('8.255.4.25')) == True
    assert(validate('25.275.25.25')) == False
    assert(validate('25.-25.25.25')) == False
    assert(validate('300.25.25')) == False

def test_thrd():
    assert(validate('25.35.255.25')) == True
    assert(validate('22.25.0.25')) == True
    assert(validate('1.25.-25.25')) == False
    assert(validate('25.25.300.25')) == False
    assert(validate('300')) == False

def test_frth():
    assert(validate('25.47.25.255')) == True
    assert(validate('58.25.13.0')) == True
    assert(validate('25.25.0.-4')) == False
    assert(validate('25.25.0.354')) == False
    assert(validate('300.25')) == False