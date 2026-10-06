# [Python] Two hash tables

> Author: Benhao
> Date: 2024-03-21
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2671. 频率跟踪器](https://leetcode.cn/problems/frequency-tracker/description/)

[TOC]

# Intuition

> One hash table maps each number to its frequency; the other maps each frequency to the number of values with that frequency.

# Approach

> Whenever a number's frequency changes, update the frequency-count table accordingly.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
