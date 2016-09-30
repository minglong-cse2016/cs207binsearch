
from pytest import raises
from binsearch import binary_search

def test_binary_search():
    assert binary_search([0, 5, 6], 6) == 2

def test_char():
    with raises(TypeError):
        binary_search(['a', 3], 3)

def test_no_input():
    with raises(TypeError):
        binary_search()

def test_empty_input():
    assert binary_search([], 1) == -1

def test_one_input():
    assert binary_search([5], 10) == -1

def test_two_input():
    assert binary_search([5, 10], 3) == -1
    
def test_left_boundary():
    assert binary_search([1, 2, 3, 4], -1) == -1

def test_middle():
    assert binary_search([1, 2, 8, 10], 5) == -1

def test_right_boundary():
    assert binary_search([1, 2, 3, 4], 10) == -1

    
    
#def test_zero_median():
#    with raises(ValueError):
#        mymedian([])
        
#def test_char_median():
#    with raises(TypeError):
#        mymedian(['a', 3])