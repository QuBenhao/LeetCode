# [Python3] Count each number minus its digit reversal

> Author: Benhao
> Date: 2021-04-03
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])
Count occurrences of each number minus its reversal, then use the formula for choosing two from n.

### Code

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
