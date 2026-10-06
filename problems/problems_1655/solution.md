# [Python] Greedy memoized search

> Author: Benhao
> Date: 2021-06-10
> Upvotes: 0
> Tags: Python, Python3

---

### Approach
Count number frequencies, sort them in descending order, and keep the first `len(quantity)` counts. If these largest counts cannot satisfy the requests, adding smaller ones cannot help.
Store the available counts in a tuple and enumerate valid allocations at each step.

### Code

```python3
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = Counter(nums)
        m = len(quantity)
        options = [val for val in c.values()]
        options.sort(reverse=True)

        @lru_cache(None)
        def dfs(idx, ops):
            if idx == m:
                return True
            if ops[0] < quantity[idx]:
                return False
            
            for i in range(len(ops)):
                if ops[i] < quantity[idx]:
                    break
                temp = list(ops)
                temp[i] -= quantity[idx]
                temp.sort(reverse=True)
                if dfs(idx+1, tuple(temp)):
                    return True
            return False
        
        return dfs(0, tuple(options[:m]))
```
