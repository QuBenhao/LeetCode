# [Python] Simulation

> slug: python-mo-ni-by-himymben-4ocn
> date: 2022-03-06
> tags: Python, Python3
> question: Append K Integers With Minimal Sum (append-k-integers-with-minimal-sum)
> url: https://leetcode.cn/problems/append-k-integers-with-minimal-sum/solutions/Aguts3/python-mo-ni-by-himymben-4ocn/

---
### Approach
After sorting, fill gaps from smallest to largest and compute each sum directly with the arithmetic-series formula.

A shorter solution accumulates the sum of encountered values while increasing k, then applies the arithmetic-series formula once and subtracts that accumulated sum.

### Code

```python3
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, last = 0, 0 if nums[0] != 1 else 1
        for num in nums:
            if not k:
                break
            if num == last:
                continue
            elif num > last + 1:
                diff = num - 1 - last
                if k < diff:
                    ans += (last + 1 + last + k) * k // 2
                else:
                    ans += (last + num) * diff // 2
                k -= min(diff, k)
            last = num
        if k:
            ans += (last + 1 + last + k) * k // 2
        return ans
```
