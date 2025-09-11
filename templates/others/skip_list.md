# 跳表

[Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)

跳表是一种**多层链表结构**，通过建立多级索引实现快速查询（时间复杂度 $`O(\log n)`$），常用于代替平衡树。Redis 的有序集合（Sorted
Set）底层即使用跳表。

```python
import random
from typing import Optional


class SkipNode:
    def __init__(self, val: int = -1, levels: int = 0):
        self.val = val
        self.next = [None] * levels  # 每层的下一个节点


class SkipList:
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level  # 最大层数
        self.p = p  # 层数生成概率
        self.head = SkipNode(levels=self.max_level)
        self.level = 0  # 当前有效层数

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


# 使用示例
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
	maxLevel = 16     // 最大层数
	p        = 0.5    // 层数生成概率
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

// 使用示例
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

## **核心特性**

1. **多层结构**：包含多个层级的链表，底层链表包含所有元素，上层链表作为索引。
2. **随机层数**：插入节点时，随机生成层数（概率控制，通常为 50%）。
3. **快速查询**：从高层向低层逐级缩小范围，类似二分查找。

## **时间复杂度**

| 操作 | 时间复杂度         |
|----|---------------|
| 查找 | $`O(\log n)`$ |
| 插入 | $`O(\log n)`$ |
| 删除 | $`O(\log n)`$ |

## **关键操作解析**

| 操作     | 步骤                                               |
|--------|--------------------------------------------------|
| **插入** | 1. 查找插入位置并记录每层的前驱节点；<br>2. 随机生成层数；<br>3. 更新各层指针。 |
| **删除** | 1. 查找目标节点并记录每层的前驱节点；<br>2. 更新指针并调整有效层数。          |
| **查找** | 从最高层开始，逐层缩小范围，最终在底层定位。                           |

## **应用场景**

1. **有序集合**：如 Redis 的 `ZSET`，支持快速范围查询。
2. **替代平衡树**：实现简单且在高并发环境下性能更好。
3. **高性能索引**：需要频繁插入、删除和查询的场景。

通过跳表的结构设计和随机层数生成，可以在保证高效操作的同时避免复杂的平衡调整逻辑。
