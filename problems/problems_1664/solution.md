# [Python] Prefix sums by index parity

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Deleting an element preserves index parity on its left and flips parity on its right. Separate prefix sums for even and odd indices let us check equality after deleting any element in o(1).

### Code

```python3
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Compare sums at odd and even indices; deleting one number flips the parity of later indices
        n = len(nums)
        odds = [0] * (n + 2)
        evens = [0] * (n + 2)
        for i,num in enumerate(nums):
            if i % 2 == 0:
                evens[i] = evens[i-2] + num
                odds[i] = odds[i-1]
            else:
                odds[i] = odds[i-2] + num
                evens[i] = evens[i-1]
        # print(evens, odds)
        ans = 0
        for i in range(n):
            # New odd sum = odd sum left of i + even sum right of i; the even sum is the reverse
            if odds[i-1] + evens[n-1] - evens[i] == odds[n-1] - odds[i] + evens[i-1]:
                ans += 1
        return ans
```

I learned an alternative that uses positive and negative signs to distinguish parity.
```python3
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Difference between the even-index and odd-index sums
        delta = sum(nums[0::2]) - sum(nums[1::2])
        # Sign
        flag = 1
        res = 0
        # Current sum
        cur = 0
        for i, num in enumerate(nums):
            # Subtract twice the preceding sum to flip its signs: added even values become subtractions, and subtracted odd values become additions
            if delta - 2 * cur - flag * num == 0:
                res += 1
            cur += flag * num
            flag *= -1
        return res
```
