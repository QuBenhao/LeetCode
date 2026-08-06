# [Python] 双指针模拟

> slug: python-shuang-zhi-zhen-mo-ni-by-himymben-satv
> date: 2021-08-22
> tags: Python, Python3
> question: Strobogrammatic Number (strobogrammatic-number)
> url: https://leetcode.cn/problems/strobogrammatic-number/solutions/vH7u6c/python-shuang-zhi-zhen-mo-ni-by-himymben-satv/

---
### 解题思路
左右双指针必须满足翻转对称关系

### 代码

```python3
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 满足旋转后还是数字的数字
        reverseDict = {'6':'9','9':'6','8':'8','0':'0','1':'1'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in reverseDict or num[r] not in reverseDict or reverseDict[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

```