import heapq

# original heap implementation: 
# https://hg.python.org/cpython/file/2.7/Lib/heapq.py

## resource: https://www.youtube.com/watch?v=WsNQuCa_-PU

class Heap:
    def __init__(self, array, key=lambda x: x):
        self._key = key
        self.array = array

    def _siftdown(self, startpos, pos):
        pass

    def _siftup(self, pos):
        pass

    def push(self, x):
        pass

    def pop(self, x):
        pass

    def heapify(self, key=None):
        pass


    ## https://docs.python.org/2.7/reference/datamodel.html
    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        pass

