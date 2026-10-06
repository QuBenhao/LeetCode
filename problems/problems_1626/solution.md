# [Py] Sorting and dynamic programming

> slug: py-pai-xu-dong-tai-gui-hua-by-himymben-4tbl
> date: 2023-03-22
> tags: Python3
> question: Best Team With No Conflicts (best-team-with-no-conflicts)
> url: https://leetcode.cn/problems/best-team-with-no-conflicts/solutions/uuMZwr/py-pai-xu-dong-tai-gui-hua-by-himymben-4tbl/

---
```python3
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        # dp[i] is the maximum score obtainable when choosing player i
        dp = [0] * len(players)
        for i, (s, a) in enumerate(players):
            for j in range(i):
                # To avoid conflicts with player i, earlier chosen players must be no older (sorting handles scores)
                if players[j][1] <= a:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += s
        return max(dp)
```
