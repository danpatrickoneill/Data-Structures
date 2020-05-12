class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.next = next

  def insert_after(self, value):
    temp = self.next
    self.next = ListNode(value, self, temp)

  def delete(self):
    pass

class SinglyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    new_head = ListNode(value)
    new_head.next = self.head
    self.head = new_head
    if not self.tail:
      self.tail = self.head

  def remove_from_head(self):
    if not self.head:
      print("SLL is empty.")
      return None
    temp = self.head.value
    self.head = self.head.next
    return temp

  def add_to_tail(self, value):
    new_tail = ListNode(value)
    if self.tail:
      self.tail.next = new_tail
    self.tail = new_tail
    if not self.head:
      self.head = self.tail

  def remove_from_tail(self):
    if not self.tail:
      print("SLL is empty.")
      return None
    temp = self.tail.value
    self.tail = None
    return temp


