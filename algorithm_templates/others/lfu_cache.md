# LFU cache

**Least frequently used algorithm**

This caching algorithm uses a counter to track how often each entry is accessed. LFU evicts the entries with the lowest access counts first. It is not commonly used because an entry that was accessed frequently at first may remain cached long after its last access.

Hash table + doubly linked lists + frequency tracking

```python
from collections import defaultdict
from typing import Optional


class Node:
    # Speed up attribute access and save memory
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'

    def __init__(self, key=0, val=0):
        self.key = key
        self.value = val
        self.freq = 1  # A new book has been read once


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        def new_list() -> Node:
            dummy = Node()  # Sentinel node
            dummy.prev = dummy
            dummy.next = dummy
            return dummy

        self.freq_to_dummy = defaultdict(new_list)
        self.min_freq = 0

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # This book is absent
            return None
        node = self.key_to_node[key]  # This book is present
        self.remove(node)  # Pull this book out
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:  # The stack of books is empty after removal
            del self.freq_to_dummy[node.freq]  # Remove the empty linked list
            if self.min_freq == node.freq:  # This is the leftmost stack of books
                self.min_freq += 1
        node.freq += 1  # Increment the number of reads
        self.push_front(self.freq_to_dummy[node.freq], node)  # Place it on top of the stack to the right
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:  # This book is present
            node.value = value  # Update value
            return
        if len(self.key_to_node) == self.capacity:  # Too many books
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev  # Bottom book in the leftmost stack
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # Remove it
            if dummy.prev == dummy:  # This stack of books is empty
                del self.freq_to_dummy[self.min_freq]  # Remove the empty linked list
        self.key_to_node[key] = node = Node(key, value)  # A new book
        self.push_front(self.freq_to_dummy[1], node)  # Place it on top of the stack of books read once
        self.min_freq = 1

    # Remove a node (pull out a book)
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # Add a node at the head of the list (place a book on top)
    def push_front(self, dummy: Node, x: Node) -> None:
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x
```
