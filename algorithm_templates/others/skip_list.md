# Skip list

[Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)

A skip list is a **multilevel linked list** that uses several index levels for fast queries (time complexity $`O(\log n)`$). It is often used as an alternative to balanced trees. Redis sorted
sets use skip lists internally.

```python
import random
from typing import Optional


class SkipNode:
    def __init__(self, val: int = -1, levels: int = 0):
        self.val = val
        self.next = [None] * levels  # Next node at each level


class SkipList:
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level  # Maximum number of levels
        self.p = p  # Probability of adding another level
        self.head = SkipNode(levels=self.max_level)
        self.level = 0  # Current number of active levels

    def _random_level(self) -> int:
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def search(self, target: int) -> bool:
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * (self.max_level)
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level, new_level):
                update[i] = self.head
            self.level = new_level
        new_node = SkipNode(num, new_level)
        for i in range(new_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        if not curr or curr.val != num:
            return False
        for i in range(self.level):
            if update[i].next[i] != curr:
                break
            update[i].next[i] = curr.next[i]
        while self.level > 0 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return True


# Usage example
sl = SkipList()
sl.add(3)
sl.add(1)
sl.add(2)
print(sl.search(2))  # True
sl.erase(2)
print(sl.search(2))  # False
```

```go
package main

import (
	"math/rand"
	"time"
)

const (
	maxLevel = 16     // Maximum number of levels
	p        = 0.5    // Probability of adding another level
)

type SkipNode struct {
	val  int
	next []*SkipNode
}

type SkipList struct {
	head  *SkipNode
	level int
}

func NewSkipList() *SkipList {
	rand.Seed(time.Now().UnixNano())
	return &SkipList{
		head:  &SkipNode{next: make([]*SkipNode, maxLevel)},
		level: 0,
	}
}

func (sl *SkipList) randomLevel() int {
	level := 1
	for rand.Float64() < p && level < maxLevel {
		level++
	}
	return level
}

func (sl *SkipList) Search(target int) bool {
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < target {
			curr = curr.next[i]
		}
	}
	curr = curr.next[0]
	return curr != nil && curr.val == target
}

func (sl *SkipList) Add(num int) {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	newLevel := sl.randomLevel()
	if newLevel > sl.level {
		for i := sl.level; i < newLevel; i++ {
			update[i] = sl.head
		}
		sl.level = newLevel
	}
	newNode := &SkipNode{
		val:  num,
		next: make([]*SkipNode, newLevel),
	}
	for i := 0; i < newLevel; i++ {
		newNode.next[i] = update[i].next[i]
		update[i].next[i] = newNode
	}
}

func (sl *SkipList) Erase(num int) bool {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	curr = curr.next[0]
	if curr == nil || curr.val != num {
		return false
	}
	for i := 0; i < sl.level; i++ {
		if update[i].next[i] != curr {
			break
		}
		update[i].next[i] = curr.next[i]
	}
	for sl.level > 0 && sl.head.next[sl.level-1] == nil {
		sl.level--
	}
	return true
}

// Usage example
func main() {
	sl := NewSkipList()
	sl.Add(3)
	sl.Add(1)
	sl.Add(2)
	println(sl.Search(2)) // true
	sl.Erase(2)
	println(sl.Search(2)) // false
}
```

## **Core properties**

1. **Multilevel structure**: Several linked-list levels are used. The bottom level contains every element, while the upper levels serve as indexes.
2. **Random levels**: Each inserted node receives a random number of levels, controlled by a probability that is usually 50%.
3. **Fast queries**: Narrow the search from higher levels to lower ones, similarly to binary search.

## **Time complexity**

| Operation | Time complexity |
|----|---------------|
| Search | $`O(\log n)`$ |
| Insert | $`O(\log n)`$ |
| Delete | $`O(\log n)`$ |

## **Key operations**

| Operation | Steps |
|--------|--------------------------------------------------|
| **Insert** | 1. Find the insertion position and record the predecessor at each level.<br>2. Generate a random number of levels.<br>3. Update the pointers at each level. |
| **Delete** | 1. Find the target node and record the predecessor at each level.<br>2. Update the pointers and adjust the number of active levels. |
| **Search** | Start at the highest level and narrow the search one level at a time, locating the element at the bottom level. |

## **Applications**

1. **Sorted sets**: For example, Redis `ZSET` supports fast range queries.
2. **Alternative to balanced trees**: Simpler to implement and performs better under high concurrency.
3. **High-performance indexes**: Suitable for frequent insertions, deletions, and queries.

A skip list's structure and random level generation support efficient operations without complex rebalancing logic.
