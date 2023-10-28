# Queue implementation using an array
# Elements are waiting in line: first in first out (served)
# Add (waiting) element at the end: enqueue, O(1) amortized
# Serve (waiting) element at the front: dequeue, O(1) amortized

class Empty(Exception):
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        """Create an empty quque."""
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
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
    
    def dequeue(self) -> object:
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
    
    def enqueue(self, e: object):
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
        # Start copy old data
        walk = self._front  # self._front may not be index 0 in self._data
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    # Test __init__()
    q1 = ArrayQueue()

    # Test enqueue()
    # There should be a resize
    for i in range(15):
        q1.enqueue(i)
    print("q1._data:", q1._data)

    # Test dequeue()
    for i in range(10):
        q1.dequeue()
    print("q1._data:", q1._data)

    # There should be a resize
    q1.dequeue()
    print("q1._data:", q1._data)

    q1.dequeue()
    print("q1._data:", q1._data)

    q1.dequeue()
    print("q1._data:", q1._data)

    # Test enqueue()
    for i in range(7):
        q1.enqueue(i)

    print("q1._data:", q1._data)
    q1.enqueue(7)
    print("q1._data:", q1._data)

    # There should be a resize
    q1.enqueue(8)
    print("q1._data:", q1._data)
