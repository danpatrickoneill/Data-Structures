from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue(DoublyLinkedList):
    def __init__(self, node=None):
        super().__init__(node)
        # self.size = self.length
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.add_to_tail(value)
        # self.size += 1

    def dequeue(self):
        if self.length == 0:
            return None
        # self.size -= 1
        return self.remove_from_head()

    def len(self):
        return self.length
