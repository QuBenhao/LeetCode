# [Python] 忘了哪次竞赛做的了,贪心就行了

> Author: Benhao
> Date: 2021-07-01
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
题目要尽可能多地买雪糕，自然是每次买雪糕花的钱越少越好

### 代码

```python3
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        idx = 0
        while coins > 0 and idx < len(costs) and costs[idx] <= coins:
            coins -= costs[idx]
            idx += 1
        return idx
```
```python3
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        ans = 0
        while coins and costs:
            if coins < costs[0]:
                break
            coins -= heapq.heappop(costs)
            ans += 1
        return ans
```