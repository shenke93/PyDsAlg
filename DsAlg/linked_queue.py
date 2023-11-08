# Queue implementation using a singly linked list.

class Empty(Exception):
    pass

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    #--------------------- nested _Node class -----------------
    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element: object, next: object) -> None:
            self._element = element
            self._next = next
    
    #-------------------- queue methods ----------------------
    def __init__(self) -> None:
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0  # numbef of queue elements

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if queue is empty."""
        return self._size == 0
    
    def first(self) -> object:
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def dequeue(self) -> object:
        """Remove and return the first element of the queue.
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')    
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None 
        return answer

    def enqueue(self, e: object) -> None:
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)    # will be the new tail 
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

if __name__ == '__main__':
    S = LinkedQueue()                 # contents: [ ]
    S.enqueue(5)                        # contents: [5]
    S.enqueue(3)                        # contents: [5, 3]
    print(len(S))                    # contents: [5, 3];    outputs 2
    print(S.dequeue())                   # contents: [3];       outputs 5
    print(S.is_empty())              # contents: [3];       outputs False
    print(S.dequeue())                   # contents: [ ];       outputs 3
    print(S.is_empty())              # contents: [ ];       outputs True
    exit()
    S.push(7)                        # contents: [7]
    S.push(9)                        # contents: [7, 9]
    print(S.top())                   # contents: [7, 9];    outputs 9
    S.push(4)                        # contents: [7, 9, 4]
    print(len(S))                    # contents: [7, 9, 4]; outputs 3
    print(S.pop())                   # contents: [7, 9];    outputs 4
    S.push(6)                        # contents: [7, 9, 6]
    S.push(8)                        # contents: [7, 9, 6, 8]
    print(S.pop())                   # contents: [7, 9, 6]; outputs 8