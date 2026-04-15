# [Python] 双哈希

> Author: Benhao
> Date: 2024-03-21
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2671. 频率跟踪器](https://leetcode.cn/problems/frequency-tracker/description/)

[TOC]

# 思路

> 一个哈希记录数字和它的频次，另一个哈希记录频次和有这个频次的数量

# 解题方法

> 在数字频次进行变化时，对频次的哈希进行同步变化即可

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class FrequencyTracker:

    def __init__(self):
        self.counter = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        self.freq[self.counter[number]] -= 1
        self.counter[number] += 1
        self.freq[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.counter:
            self.freq[self.counter[number]] -= 1
            self.counter[number] -= 1
            self.freq[self.counter[number]] += 1
            if not self.counter[number]:
                self.counter.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
```
  
