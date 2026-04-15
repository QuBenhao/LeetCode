# [Python] Hash表后的二分查找

> Author: Benhao
> Date: 2021-03-13
> Upvotes: 1
> Tags: Python

---

### 解题思路
HashMap也用同样思路实现过，因为key总是独特的，排序以后便于查找
详见[HashMap](https://leetcode.cn/problems/design-hashmap/solution/ha-xi-biao-zhong-shi-yong-shuang-xiang-l-fcw7/)

### 代码

```python
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_key = 2069
        self.arr = [None] * self.hash_key

    def hash(self, key):
        return key % self.hash_key

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = self.hash(key)
        if not self.arr[k]:
            self.arr[k] = [key]
        else:
            index = self.binary_search(key)
            if index < len(self.arr[k]):
                if self.arr[k][index] == key:
                    return
                elif self.arr[k][index] < key:
                    self.arr[k].insert(index + 1, key)
                elif self.arr[k][index] > key:
                    self.arr[k].insert(index, key)
            else:
                self.arr[k].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        k = self.hash(key)
        if self.arr[k]:
            index = self.binary_search(key)
            if index < len(self.arr[k]) and self.arr[k][index] == key:
                self.arr[k] = self.arr[k][:index] + self.arr[k][index+1:]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        k = self.hash(key)
        if self.arr[k]:
            index = self.binary_search(key)
            if index < len(self.arr[k]) and self.arr[k][index] == key:
                return True
        return False

    def binary_search(self, key):
        k = self.hash(key)
        left, right = 0, len(self.arr[k])
        while left < right:
            mid = (left + right) // 2
            if self.arr[k][mid] == key:
                return mid
            elif self.arr[k][mid] > key:
                right = mid
            else:
                left = mid + 1
        return left


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

```