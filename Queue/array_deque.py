# Double-ended queue implementation using an array
# Elements are waiting in line: first in first out (served)
# Add (waiting) element at the end: add_last, O(1) amortized
# Serve (waiting) element at the front: delete_first, O(1) amortized
# Add (waiting) element at the front: add_first, O(1) amortized
# Serve (waiting) element at the end: delete_last, O(1) amortized


class Empty(Exception):
    pass

class ArrayDeque:
    """Double-ended queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        """Create an empty quque."""
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0  # size of queue (number of elements)
        self._front = 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return Ture if the queue is empty."""
        return self._size == 0
    
    def first(self) -> object:
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def last(self) -> object:
        """Return (but do not remove) the element at the back of the queue.
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self) -> object:
        """Remove and return the first element of the queue.
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def delete_last(self) -> object:
        """Remove and return the last element of the deque.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None      # help garbage collection
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def add_first(self, e: object):
        """Add an element to the begining of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        print("in add_first, self._front:", self._front)
        avail = self._front
        self._data[avail] = e
        self._size += 1
        

    def add_last(self, e: object):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):   # not enough capacity
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap: int):    # we assume cap >= len(self)
        """Resize to a new list of capacity."""
        old = self._data
        self._data = [None] * cap
        # Start copy old data into the new array
        walk = self._front  # self._front may not be index 0 in self._data
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    # Test __init__()
    q1 = ArrayDeque()

    # Test enqueue()
    # There should be a resize
    for i in range(15):
        q1.add_last(i)
    print("q1._data:", q1._data)

    # Test dequeue()
    for i in range(10):
        q1.delete_first()
    print("q1._data:", q1._data)

    # There should be a resize
    q1.delete_first()
    print("q1._data:", q1._data)

    q1.delete_first()
    print("q1._data:", q1._data)

    q1.delete_first()
    print("q1._data:", q1._data)

    # Test enqueue()
    for i in range(7):
        q1.add_last(i)

    print("q1._data:", q1._data)
    q1.add_last(7)
    print("q1._data:", q1._data)

    # There should be a resize
    q1.add_last(8)
    print("q1._data:", q1._data)
    print("q1._front:", q1._front)
    print("q1.first()", q1.first())

    q1.add_first('a')
    print("q1._data:", q1._data)
    print("q1._front:", q1._front)
    print("q1.first()", q1.first())

    q1.add_first('b')
    print("q1._data:", q1._data)
    print("q1._front:", q1._front)
    print("q1.first()", q1.first())

    q1.delete_last()
    print("q1._data:", q1._data)
    print("q1._size:", q1._size)

    q1.delete_last()
    print("q1._data:", q1._data)
    print("q1._size:", q1._size)

    q1.add_first('c')
    print("q1._data:", q1._data)
    print("q1._front:", q1._front)
    print("q1.first()", q1.first())


