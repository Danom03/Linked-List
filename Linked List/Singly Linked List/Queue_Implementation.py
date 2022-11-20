class Empty(Exception):
    """Returns Error if Queue is Empty"""
    pass

class LinkedQueue:
    """Queue Implementation using Linked List"""

    class _Node:
        """Lightweight, non-public, nested class to store element of the Node and maintain reference of the next Node"""

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Returns Length of the Queue"""
        return self._size

    def is_empty(self):
        """Returns whether Queue is Empty or Not"""
        return self._size == 0

    def first(self):
        """Returns First Element(head) of the Queue."""
        if self.is_empty():
            return Empty("Queue is Empty!")
        return self._head._element

    def enqueue(self, e):
        """Adds new element e into the Queue at tail"""
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Removes First element from the Queue"""
        if self.is_empty():
            return Empty('Queue is Empty!')

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return answer
