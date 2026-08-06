# [Python] 模拟

> slug: python-mo-ni-by-himymben-yqzr
> date: 2022-02-06
> tags: Python, Python3
> question: Smallest Value of the Rearranged Number (smallest-value-of-the-rearranged-number)
> url: https://leetcode.cn/problems/smallest-value-of-the-rearranged-number/solutions/9cgvJq/python-mo-ni-by-himymben-yqzr/

---
### 解题思路
正数重排尽可能小，负数重排尽可能大

### 代码

```python3
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            start = -num
        else:
            start = num
        cnts = [0] * 10
        while start:
            cnts[start%10] += 1
            start //= 10
        ans = 0
        if num < 0:
            for i in range(9, -1, -1):
                for j in range(cnts[i]):
                    ans *= 10
                    ans += i
            return -ans
        else:
            for i in range(1, 10):
                if cnts[i]:
                    ans += i
                    cnts[i] -= 1
                    break
            for i in range(10):
                for j in range(cnts[i]):
                    ans *= 10
                    ans += i
            return ans

```