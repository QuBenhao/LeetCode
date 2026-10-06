# LRU cache

**Least recently used algorithm**

A doubly linked list and a hash table whose values are list nodes

```python
from typing import Optional


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
        self.key_to_node = {}

    # Get the node for key and move it to the head of the list
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # This book is absent
            return None
        node = self.key_to_node[key]  # This book is present
        self.remove(node)  # Pull this book out
        self.push_front(node)  # Place it on top
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)  # get_node moves the corresponding node to the head of the list
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)  # get_node moves the corresponding node to the head of the list
        if node:  # This book is present
            node.value = value  # Update value
            return
        self.key_to_node[key] = node = Node(key, value)  # A new book
        self.push_front(node)  # Place it on top
        if len(self.key_to_node) > self.capacity:  # Too many books
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # Remove the last book

    # Remove a node (pull out a book)
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # Add a node at the head of the list (place a book on top)
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x
```

```golang
package main

import (
    "container/list"
)

type entry struct {
    key, value int
}

type LRUCache struct {
    capacity  int
    list      *list.List // Doubly linked list
    keyToNode map[int]*list.Element
}

func Constructor(capacity int) LRUCache {
    return LRUCache{capacity, list.New(), map[int]*list.Element{}}
}

func (c *LRUCache) Get(key int) int {
    node := c.keyToNode[key]
    if node == nil { // This book is absent
        return -1
    }
    c.list.MoveToFront(node) // Place this book on top
    return node.Value.(entry).value
}

func (c *LRUCache) Put(key, value int) {
    if node := c.keyToNode[key]; node != nil { // This book is present
        node.Value = entry{key, value} // Update
        c.list.MoveToFront(node) // Place this book on top
        return
    }
    c.keyToNode[key] = c.list.PushFront(entry{key, value}) // Place the new book on top
    if len(c.keyToNode) > c.capacity { // Too many books
        delete(c.keyToNode, c.list.Remove(c.list.Back()).(entry).key) // Remove the last book
    }
}
```
