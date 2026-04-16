# [Python] 关键在于遍历下一个情况两个运动员的位置

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
参考自[代码](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/discuss/1268452/Python-2-Solution%3A-dfs-and-smart-dp-explained)

### 代码

```python3
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(l, r, m):
            if l > r:
                return dp(r, l, m)
            # 两个人到达同一位置(即他俩发生了对抗)
            if l == r:
                return 1, 1

            earliest, latest = inf, 0
            # l的下一个可能性为1(l前面的全部为负)到l(l前面的全部为胜)
            for i in range(1, l + 1):
                # r的下一个可能性为l-i+1 (r到l之间的全部为负)到r-i (r到l之间的全部为胜)
                for j in range(l - i + 1, r - i + 1):
                    if not (m + 1) // 2 >= i + j >= l + r - m // 2:
                        continue
                    ea, la = dp(i, j, (m + 1) // 2)
                    earliest = min(earliest, ea + 1)
                    latest = max(latest, la + 1)
            return earliest, latest

        return list(dp(firstPlayer, n - secondPlayer + 1, n))
```