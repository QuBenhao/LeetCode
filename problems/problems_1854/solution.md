# [Python] 模拟

> Author: Benhao
> Date: 2021-05-09
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
作为一个没有感情的人口统计机器，每当某年有人出生，该年的人数要+1，每当某年有人死亡，该年的人数要-1。每年的人口变化为1950年到2050年的数组。
而从始至终就可以统计每年有多少人，活着。

### 代码

```python3
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = [0] * 101
        base_year = 1950
        for b,d in logs:
            people[b-base_year] += 1
            people[d-base_year] -= 1
        curr = ans = m = 0
        for i,p in enumerate(people):
            curr += p
            if curr > m:
                m, ans = curr, base_year + i
        return ans
```