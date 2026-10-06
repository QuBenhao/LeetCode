import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = LRUCache(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class Node:
    # Speed up attribute access and save memory
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # Sentinel node
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # This book is not present
            return None
        node = self.key_to_node[key]  # This book is present
        self.remove(node)  # Take this book out
        self.push_front(node)  # Put it on top
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:  # This book is present
            node.value = value  # Update value
            return
        self.key_to_node[key] = node = Node(key, value)  # New book
        self.push_front(node)  # Put it on top
        if len(self.key_to_node) > self.capacity:  # Too many books
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # Remove the last book

    # Remove a node (take out a book)
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # Add a node at the head of the list (put a book on top)
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
