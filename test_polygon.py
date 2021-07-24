import pytest
from polygon_sequence import Polygon_sequence as Polygon_sequence

######------ Testing if Polygon sequence is iterable-------
def test_polygon_sequence():
    n = 6
    R = 10
    p = Polygon_sequence(n, R)
    p_iter = iter(p)


    assert '__iter__' in p_iter.__dir__(), "iterator is not defined"
    assert '__next__' in dir(p_iter), "iterator should have __next__"
    assert '__iter__' in dir(p), "iterable should have __iter__"
    assert '__next__' not in dir(p), "iterable need not have __next__"

    assert id(p) != id(p_iter)," polygon_sequence is not an iterable!!!!"
    assert id(p_iter) == id(iter(p_iter)), " polygon_sequence is not an iterable!!!!"


    for i in range(n-2):
        string = str(next(p_iter))
        assert string == f'Polygon(n={i+3}, R=10)',"----"

    with pytest.raises(StopIteration):
        next(p_iter)
