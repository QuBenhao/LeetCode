# [Python] 动态规划

> Author: Benhao
> Date: 2021-04-11
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
维护到达i时，三条跑道处所用的最小跳跃值。
每次跳的时候，讨论当前位置的障碍物和下一个位置的障碍物。
我们想从两个障碍物中交错通过时，总是需要两次跳跃；
而我们想从两侧前面没有障碍物的地方跳到当前障碍物的前面时，总是需要一次跳跃；
最后如果前面没有障碍物，不需要跳跃。

### 代码

```python3
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        ans = [1, 0, 1]
        for i in range(1,n-1):
            new = [float("inf")] * 3
            for j in range(3):
                for k in range(3):
                    if j == obstacles[i-1] - 1 and k == obstacles[i] - 1:
                        new[j] = min(ans[k] + 2, new[j])
                    elif j == obstacles[i - 1] - 1:
                        new[j] = min(ans[k] + 1, new[j])
                    elif k != obstacles[i] - 1 and j == k:
                        new[j] = min(ans[j], new[j])
            ans = new
        return min(ans)

```