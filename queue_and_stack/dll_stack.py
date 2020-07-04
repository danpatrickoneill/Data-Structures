from doubly_linked_list import DoublyLinkedList
from singly_linked_list import SinglyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = SinglyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_from_head()
        return None

    def len(self):
        return self.size
    # pass