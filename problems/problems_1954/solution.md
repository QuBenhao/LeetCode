# [Python] 递推公式 + 二分查找

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
第i层都比第i-1层多了一个外圈，外圈计算一下可知是$12 * i^2$个苹果。
由f(i) - f(i-1) = 12 * i * i, f(0) = 0 可得:
f(i) = 2 * i * (i+1) * (2*i+1)。
我们二分查找需要的层数即可。

### 代码

```python3
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # f(i) = f(i-1) + 12 * i + 8 * (i+1 + i+2 + ... + 2*i-1) = f(i-1) + 12 * i * i
        # f(i) = 12 * 1^2 + 12 * 2^2 + ... + 12 * i^2 = 2 * n* (n+1) * (2n+1)
        def f(i):
            return 2 * i * (i+1) * (2*i+1)

        # f(62996) >= 10 ** 15
        left, right = 1, 63000
        while left < right:
            mid = left + right >> 1
            if f(mid) < neededApples:
                left = mid + 1
            else:
                right = mid
        return 8 * left

```