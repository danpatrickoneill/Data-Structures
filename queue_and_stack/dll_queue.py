from doubly_linked_list import DoublyLinkedList
from singly_linked_list import SinglyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = SinglyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        # print(f"Enqueued successfully; queue size is now {self.size}")

    def dequeue(self):
        print(self.size, self.size > 0)
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        return None

    def len(self):
        return self.size

q = Queue()
q.enqueue(1)