# [Python3] 统计自己减自己的转置即可

> Author: Benhao
> Date: 2021-04-03
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])
所以只要统计每个数减去自己的转置的个数，用n个里面取2个的公式计算结果即可

### 代码

```python3
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:            
            
        mod = 10 ** 9 + 7
        d = Counter()
        for n in nums:
            d[n - int(str(n)[::-1])] += 1
        ans = 0
        for k in d:
            ans += d[k] * (d[k] - 1) // 2
        return ans % mod
```