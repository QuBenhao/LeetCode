# [Python] 记忆化递归

> slug: python-ji-yi-hua-di-gui-by-himymben-i27f
> date: 2021-11-27
> tags: Python, Python3
> question: Minimum Number of Food Buckets to Feed the Hamsters (minimum-number-of-food-buckets-to-feed-the-hamsters)
> url: https://leetcode.cn/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/solutions/kSLrrZ/python-ji-yi-hua-di-gui-by-himymben-i27f/

---
```python3
class Solution:
    def minimumBuckets(self, street: str) -> int:
        if len(street) == 1:
            return -1 if street == "H" else 0
        
        @lru_cache(None)
        def dfs(i, last):
            if i >= len(street):
                return 0
            if street[i] == "H" and last:
                return dfs(i + 1, False)
            elif street[i] == "H":
                if i == len(street) - 1 or street[i + 1] != ".":
                    return inf
                return dfs(i + 2, True) + 1
            return min(dfs(i+1,True) + 1, dfs(i + 1, False))
        
        ans = dfs(0, False)
        return ans if ans != inf else -1
```