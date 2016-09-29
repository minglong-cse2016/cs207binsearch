
from pytest import raises
from binsearch import binary_search

def test_binary_search():
    assert binary_search([0, 5, 6], 6) == 2

#def test_char():
#    with raises(TypeError):
#        myaverage(['a',3])

#def test_mymath():
#    assert mymedian([9,3, 6]) == 6
    
#def test_zero_median():
#    with raises(ValueError):
#        mymedian([])
        
#def test_char_median():
#    with raises(TypeError):
#        mymedian(['a', 3])