# [Python] 贪心

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
想要尽可能多的周，我们要尽可能多地排进所有的工作。当我们想要加入全部最大的那个工作时，我们需要用其他工作穿插在中间使他们不相连。也就是说我们至少需要有最大值-1那么多的其他工作来隔开最大的工作。而最大的工作都能安排的时候，其他工作任意穿插在不同间隔即可。

但是如果无法隔开最大的工作，那么上限其实就由其他工作的和决定。

### 代码

```python3
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m, s = max(milestones), sum(milestones)
        return (s - m) * 2 + 1 if m > s - m else s
```