import pytest
from project import check
from project import name
from project import mandatory_columns
from project import cookify
from project import grade


def test_check():
    with pytest.raises(SystemExit):
           check('stop')
    


def test_first_name():
      assert name({"FIRST NAME": ['Matthew']}) == 'Matthew'
      assert name({'FIRST NAME': ['tommy']}) == 'Tommy'
      
def test_last_name():
    assert name({'LAST NAME': ['roberts']}) == 'Roberts'
    assert name({'LAST NAME': ['Roberts']}) == 'Roberts'

def test_full_name():
     assert name({"LAST NAME": ["fernandez"], 'FIRST NAME': ["Alberto"]}) == 'Alberto Fernandez'
     assert name({"FIRST NAME": ["alberto"], 'LAST NAME': ["Fernandez"]}) == 'Alberto Fernandez'

def test_no_name():
     assert name({'GRADE' : ['0'], 'CHECK': ['matthew']}) == 'student'
          




      
def test_excel_no_email():
    with pytest.raises(SystemExit):
           mandatory_columns(['3','2','1'])
    with pytest.raises(SystemExit):
           mandatory_columns([])
     
def test_excel_no_score():
    with pytest.raises(SystemExit):
           mandatory_columns(['1','4','2'])
    with pytest.raises(SystemExit):
           mandatory_columns([])

     
def test_excel_no_email_score():
    with pytest.raises(SystemExit):
           mandatory_columns([])
    with pytest.raises(SystemExit):
           mandatory_columns(['1','2','0'])


def test_cookify():
      assert cookify(4) == '🍪🍪🍪🍪'
      assert cookify(1) == '🍪'

      

def test_grade():
      assert grade([4,4]) == 4
      assert grade([2,8]) == 5
      assert grade([1,1,8,2]) == 3
      assert grade([0,1]) == 0  
      assert grade([0,10]) == 5 
      with pytest.raises(SystemExit):
       grade(['hola'])
      



if __name__ == '__main__':
      pytest.main()