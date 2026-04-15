# [Python] 三叶姐姐教得好

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
见[三叶姐姐的363题解](https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/solution/gong-shui-san-xie-you-hua-mei-ju-de-ji-b-dh8s/)

### 代码

```python3
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(1, n + 1):
            presum = [0] * (m + 1)
            for j in range(i, n + 1):
                a = 0
                d = {0:1}
                for fixed in range(1, m + 1):
                    presum[fixed] += matrix[fixed-1][j-1]
                    a += presum[fixed]
                    if a - target in d:
                        ans += d[a - target]
                    if a in d:
                        d[a] += 1
                    else:
                        d[a] = 1
        return ans
```