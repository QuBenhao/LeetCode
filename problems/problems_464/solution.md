# [Python] 状态压缩记忆化dfs

> slug: python-zhuang-tai-ya-suo-ji-yi-hua-dfs-b-5meu
> date: 2021-08-07
> tags: Python, Python3
> question: Can I Win (can-i-win)
> url: https://leetcode.cn/problems/can-i-win/solutions/gXcL5R/python-zhuang-tai-ya-suo-ji-yi-hua-dfs-b-5meu/

---
```python3
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:        
        if sum(i for i in range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(state, curSum):
            for i in range(maxChoosableInteger):
                if not 1 << i & state:
                    if curSum + i + 1 >= desiredTotal or not dfs(1 << i | state, curSum + i + 1):
                        return True
            return False
        
        return dfs(0, 0)
```