# [Python] Two-pointer simulation

> slug: python-shuang-zhi-zhen-mo-ni-by-himymben-satv
> date: 2021-08-22
> tags: Python, Python3
> question: Strobogrammatic Number (strobogrammatic-number)
> url: https://leetcode.cn/problems/strobogrammatic-number/solutions/vH7u6c/python-shuang-zhi-zhen-mo-ni-by-himymben-satv/

---
### Approach
The left and right pointers must satisfy rotational symmetry.

### Code

```python3
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Digits that remain valid after rotation
        reverseDict = {'6':'9','9':'6','8':'8','0':'0','1':'1'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in reverseDict or num[r] not in reverseDict or reverseDict[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

```
