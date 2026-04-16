# [Python] 二分查找

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 4
> Tags: Python, Python3

---

```python3
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right=1,n
        while left < right:
            mid= (left+right)//2
            ans = guess(mid)
            if ans == -1:
                right = mid - 1
            elif ans == 1:
                left = mid +1
            else:
                return mid
        return left
```