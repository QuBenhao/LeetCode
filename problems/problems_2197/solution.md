# [Python] Stack simulation

> Author: Benhao
> Date: 2022-03-06
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Repeatedly check whether adjacent values have a greatest common divisor greater than 1; if so, merge them.
Also compare with the last element of the answer stack to merge to the left.

### Code

```python3
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        cur, i = 1, 0
        while i < len(nums):
            has = False
            if gcd(nums[i], cur) == 1:
                cur = nums[i]
            while i < len(nums) and gcd(nums[i], cur) > 1:
                cur = lcm(nums[i], cur)
                i += 1
                has = True
            while ans and gcd(ans[-1], cur) > 1:
                cur = lcm(ans.pop(), cur)
            ans.append(cur)
            if not has:
                i += 1
        return ans
```
