# [Python] Dynamic programming with rolling updates

> slug: python-dong-tai-gui-hua-gun-dong-geng-xi-x2dq
> date: 2021-07-01
> tags: Python, Python3
> question: 传递信息 (chuan-di-xin-xi)
> url: https://leetcode.cn/problems/chuan-di-xin-xi/solutions/QehSSC/python-dong-tai-gui-hua-gun-dong-geng-xi-x2dq/

---
### Approach
Use a DP array with one entry per player. dp[i] is the number of ways to reach player i in a given round.

### Code

```python3
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = defaultdict(set)
        for a,b in relation:
            graph[b].add(a)

        # Reaching n-1 from 0 in k rounds means reaching a predecessor of n-1 from 0 in k-1 rounds...
        # The recurrence sums transmissions from the predecessors of player
        # dp[k][player] = sum(dp[k-1][p']) for p' in graph[player]
        dp = [0] * n
        # Initially, player 0 has the message without any transmissions
        dp[0] = 1
        for i in range(k):
            new_dp = [0] * n
            for j in range(n):
                # All players that can transmit to j
                new_dp[j] += sum(dp[l] for l in graph[j])
            dp = new_dp
        return dp[n-1]

```
