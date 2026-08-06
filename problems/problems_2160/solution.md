# [Python] 贪心

> slug: python-tan-xin-by-himymben-mww5
> date: 2022-02-06
> tags: Python, Python3
> question: Minimum Sum of Four Digit Number After Splitting Digits (minimum-sum-of-four-digit-number-after-splitting-digits)
> url: https://leetcode.cn/problems/minimum-sum-of-four-digit-number-after-splitting-digits/solutions/mKypzE/python-tan-xin-by-himymben-mww5/

---
### 解题思路
将小的数尽量安排在前面，两个数尽可能接近最后的和最小

### 代码

```python3
class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while num:
            if (x := num % 10):
                nums.append(x)
            num //= 10
        a = b = 0
        for x in sorted(nums):
            if a > b:
                b = 10 * b + x
            else:
                a = 10 * a + x
        return a + b
```