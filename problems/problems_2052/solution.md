# [Python] 前缀和+动态规划

> slug: python-qian-zhui-he-dong-tai-gui-hua-by-31oqx
> date: 2022-05-02
> tags: Python, Python3
> question: Minimum Cost to Separate Sentence Into Rows (minimum-cost-to-separate-sentence-into-rows)
> url: https://leetcode.cn/problems/minimum-cost-to-separate-sentence-into-rows/solutions/XEPpSm/python-qian-zhui-he-dong-tai-gui-hua-by-31oqx/

---
### 解题思路
枚举左端点分割区间

### 代码

```python3
class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        words = sentence.split(' ')
        n = len(words)
        presum = [0] * (n + 1)
        for i, w in enumerate(words):
            presum[i + 1] = presum[i] + len(w)

        @lru_cache(None)
        def dfs(i):
            if presum[n] - presum[i] + n - 1 - i <= k:
                return 0
            ans, o = inf, i + 1
            while o < n and (nxt := presum[o] - presum[i] + o - 1 - i) <= k:
                ans = min(ans, (k - nxt) ** 2 + dfs(o))
                o += 1
            return ans
        
        return dfs(0)

```