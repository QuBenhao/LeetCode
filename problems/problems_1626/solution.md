# [Py] 排序动态规划

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
        # dp[i] 代表选第i个玩家时，可以选择到的最大分数
        dp = [0] * len(players)
        for i, (s, a) in enumerate(players):
            for j in range(i):
                # 选第i个玩家不能冲突，那么他以前的玩家必须是年纪小的(排序保证了分数)
                if players[j][1] <= a:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += s
        return max(dp)
```