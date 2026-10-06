# [Python] Dynamic programming

> Author: Benhao
> Date: 2021-04-11
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Track the minimum jumps needed to reach position i in each of the three lanes.
For each jump, consider obstacles at the current and next positions.
Passing between two staggered obstacles requires two jumps.
Moving from an unobstructed side lane to the position ahead of the current obstacle requires one jump.
If the path ahead is clear, no jump is needed.

### Code

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
