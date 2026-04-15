# [Python] 枚举所有配对情况

> Author: Benhao
> Date: 2021-07-26
> Upvotes: 2
> Tags: Python, Python3

---

```python3
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])

        def cal(a, b):
            return sum(a[i] == b[i] for i in range(n))

        @lru_cache(None)
        def dfs(i, mts):
            if i == m:
                return 0
            curr = list(mts)
            return max(dfs(i + 1, tuple(curr[:j] + curr[j + 1:])) + cal(students[i], mentors[curr[j]]) for j in range(len(curr)))

        return dfs(0, tuple([i for i in range(m)]))

```