class Empty(Exception):
    """Error Attempting to excess element from an Empty Stack"""
    pass


class LinkedStack:
    """Stack Implementation Using Linked List"""

# -------------------Nested Class--------------------------
    class _Node:
        """Lightweight, non-public, nested class for storing Node of Singly Linked List"""
        __slots__ = '_element', '_next'                 # Reduces Wastage of Memory

        def __init__(self, element, next):
            self._element = element                     # Element of the Node
            self._next = next                           # Reference to the next Node

# ----------------Stack Methods----------------------------
    def __init__(self):
        self._head = None                               # Reference to the head Node
        self._size = 0                                  # Number of element in the Stack

    def __len__(self):
        """Finds length of the Stack"""
        return self._size

    def is_empty(self):
        """Returns whether Stack is empty or not"""
        return self._size == 0

    def top(self):
        """Returns top element of the Stack"""

        if self.is_empty():                            # Returns Error if Stack is Empty
            return Empty("Stack is Empty")

        return self._head._element

    def push(self, e):
        """Adds element e into the Stack"""
        self._head = self._Node(e, self._head)         # Create and link a new Node
        self._size += 1

    def pop(self):
        """Removes Top(head) of the Stack"""

        if self.is_empty():                            # Returns Error if Stack is Empty
            return Empty("Stack is Empty")

        answer = self._head._element
        self._head = self._head._next                  # Assigns top to the next Node
        self._size -= 1
        return answer


def use_stack():
    S = LinkedStack()
    S.push(10)
    S.push(14)
    S.push(12)
    print(S.top())
    print(S.pop())
    print(S.is_empty())
    S.pop()
    S.pop()
    S.pop()
    S.pop()
    S.pop()
    print(S.is_empty())

# use_stack()