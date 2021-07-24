# Session-11-Assignment

######  Session was about Iterable and Iterator



Notes:

1] **Iterable's **   \__iter__  method returns an **Iterator**

2]  **Iterator's**\__iter__  method returns  **itself**

3] An Iterator has both   *\__iter__*  and   *\__next__* methods



## Assignment 

 Question: The starting point for this Assignment is the `Polygon` class and the `Polygons` sequence type  created in the previous Assignment .

Refactor the `Polygons` (sequence) type, into an **iterable**. 







***The Polygon class is same, only the Polygon_sequence class is modified with the following piece of code***

***The rest of the Polygon_sequence class is same***

#### Solution:

```python
class Polygon_sequence:

### Previous assignment
#---------------



	def __iter__(self):
        return self.PolygonIterator(self)

    class PolygonIterator:
        def __init__(self,polygon_obj):
            self.polygon_obj = polygon_obj
            self._index = 0


        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self.polygon_obj):
                raise StopIteration
            else:
                item = self.polygon_obj.sequence[self._index]
                self._index += 1
                return item
                
```





Polygon_sequence is both, a sequence_type because of `__getitem__` and an iterable because of `__iter__` method.