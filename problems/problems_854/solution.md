# [Python] 记忆化搜索

> slug: python-ji-yi-hua-sou-suo-by-himymben-q3s7
> date: 2022-09-21
> tags: Python, Python3
> question: K-Similar Strings (k-similar-strings)
> url: https://leetcode.cn/problems/k-similar-strings/solutions/WmkgXa/python-ji-yi-hua-sou-suo-by-himymben-q3s7/

---
### 解题思路
每次处理最左侧不一致的交换

### 代码

```python3
class Solution:
    @lru_cache(None)
    def kSimilarity(self, s1: str, s2: str) -> int:
        if not s1 or s1 == s2:
            return 0
        cur = [i for i in range(len(s1)) if s1[i] != s2[i]]
        candidates = [idx for idx, i in enumerate(cur) if s2[i] == s1[cur[0]]]
        ans, nxt = inf, "".join([s1[i] for i in cur[1:]])
        for c in candidates:
            cur[0], cur[c] = cur[c], cur[0]
            ans = min(ans, self.kSimilarity(nxt, "".join(s2[i] for i in cur[1:])))
            cur[0], cur[c] = cur[c], cur[0]
        return ans + 1

```