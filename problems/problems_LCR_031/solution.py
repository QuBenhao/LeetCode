import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = LRUCache(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class DoubleLinkedList:
    def __init__(self, key=-1, value=-1):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

    def insert(self, node):
        node.prev = self
        node.next = self.next
        if self.next:
            self.next.prev = node
        self.next = node

    @staticmethod
    def remove(node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        DoubleLinkedList.remove(node)
        self.tail.prev.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            DoubleLinkedList.remove(self.cache[key])
            node = self.cache[key]
            node.value = value
        else:
            if len(self.cache) == self.capacity:
                last = self.head.next
                self.cache.pop(last.key)
                DoubleLinkedList.remove(last)
            node = DoubleLinkedList(key, value)
            self.cache[key] = node
        self.tail.prev.insert(node)
