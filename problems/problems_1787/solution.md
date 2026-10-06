# [Python] Memoized search (~400ms after optimization)

> Author: Benhao
> Date: 2021-05-24
> Upvotes: 10
> Tags: Python, Python3

---

### Approach
If every length-k interval has XOR 0, then `a_0 = a_k = ...`, `a_1 = a_k+1 = ...`, and so on.
Also, `a_0 ^ a_1 ^ ... ^ a_k-1 = 0`.

All numbers in each group must become equal, so the cheapest choice is that group's mode.
Choosing every group's mode does not guarantee an overall XOR of 0, so enumerate possible changes to the groups.
`msv[idx]` is the extra cost of sacrificing this group: change every element to a value absent from the group, chosen as the XOR of the other groups so that the total XOR becomes 0.
`dfs(idx+1,curr^key)` gives the minimum changes needed afterward when this group chooses key. The extra cost over choosing its mode is `msv[idx] - counters[idx][key]`.

**Optimization** (~400ms)
Prune the search and sort candidates by the fewest required changes, favoring the mode. If the lower-bound extra cost `msv[idx] - counters[idx][key]` already exceeds `res`, skip the DFS call.

### Code

```python3
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counters = defaultdict(Counter)
        for i in range(k):
            for j in range(i, n, k):
                counters[i][nums[j]] += 1

        # Mode of each group
        msv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # Minimum cost to make each group uniform
        ans = n - sum(msv)

        # Starting from each group's mode, choose alternative values or sacrifice one group to achieve XOR 0 optimally
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # Extra cost to sacrifice this group by changing all its values to make the XOR 0
            res = msv[idx]
            # Change to a value already present in this group
            for key in counters[idx].keys():
                res = min(res, dfs(idx+1, curr ^ key) - counters[idx][key] + msv[idx])
            return res
        return ans + dfs(0, 0) 

```
Optimization
```python3
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counters = defaultdict(Counter)
        for i in range(k):
            for j in range(i, n, k):
                counters[i][nums[j]] += 1
        
        # Mode of each group
        msv = [counters[i].most_common(1)[0][1] for i in range(k)]
        # Minimum cost to make each group uniform
        ans = n - sum(msv)

        # Values in each group sorted by frequency
        keys = [sorted(counters[i].keys(),key=lambda x:-counters[i][x]) for i in range(k)]

        # Starting from each group's mode, choose alternative values or sacrifice one group to achieve XOR 0 optimally
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == k and curr == 0:
                return 0
            elif idx == k:
                return float("inf")
            # Extra cost to sacrifice this group by changing all its values to make the XOR 0
            res = msv[idx]
            # Change to a value already present in this group
            for key in keys[idx]:
                if msv[idx] - counters[idx][key] >= res:
                    continue
                res = min(res, dfs(idx+1, curr ^ key) - counters[idx][key] + msv[idx])
            return res
        return ans + dfs(0, 0)
```
