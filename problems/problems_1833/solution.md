# [Python] I forget which contest this was from; greedy works

> Author: Benhao
> Date: 2021-07-01
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
To buy as many ice creams as possible, spend as little as possible on each one.

### Code

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
