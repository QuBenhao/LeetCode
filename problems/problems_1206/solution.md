# [Python/Java/TypeScript/Go] 跳表

> Author: Benhao
> Date: 2022-07-25
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
参照[论文](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)的伪代码实现

### 代码

```Python3 []
MAX_LEVEL = 32
P = 0.25

def random_level() -> int:
    level = 1
    while level < MAX_LEVEL and random.random() < P:
        level += 1
    return level

class SkipNode:
    
    def __init__(self, value, level=MAX_LEVEL) -> None:
        self.value = value
        self.forward= [None] * level

class Skiplist:

    def __init__(self):
        self.headNode = SkipNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        return (node := self.getNode(target).forward[0]) is not None and node.value == target

    def add(self, num: int) -> None:
        update = [self.headNode] * MAX_LEVEL
        self.getNode(num, update)
        level = random_level()
        if level > self.level:
            for i in range(self.level, level):
                update[i] = self.headNode
            self.level = level
        x = SkipNode(num, level)
        for i in range(level):
            x.forward[i] = update[i].forward[i]
            update[i].forward[i] = x

    def erase(self, num: int) -> bool:
        update = [self.headNode] * MAX_LEVEL
        node = self.getNode(num, update).forward[0]
        if node and node.value == num:
            for i in range(self.level):
                if update[i].forward[i] != node:
                    break
                update[i].forward[i] = node.forward[i]
            del node
            while self.level > 0 and not self.headNode.forward[self.level - 1]:
                self.level -= 1
            return True
        return False

    def getNode(self, val: int, update=[]) -> SkipNode:
        node = self.headNode
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].value < val:
                node = node.forward[i]
            if update:
                update[i] = node
        return node

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```
```Java []
```
```TypeScript []
```
```Go []
```


(非题目要求的解法)
```Python3
class Skiplist:

    def __init__(self):
        self.map = collections.defaultdict(int)

    def search(self, target: int) -> bool:
        return target in self.map

    def add(self, num: int) -> None:
        self.map[num] += 1

    def erase(self, num: int) -> bool:
        if num in self.map:
            self.map[num] -= 1
            if not self.map[num]:
                self.map.pop(num)
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```