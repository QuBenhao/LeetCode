# [Python] 数位DP模板

> Author: Benhao
> Date: 2022-09-25
> Upvotes: 10
> Tags: Python, Python3

---

### 解题思路
当年从[草莓奶昔那里大佬学习的](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/python-shu-wei-dpmo-ban-ti-by-981377660l-xtkb/)

### 代码

```python3
def cal(upper: int, digits: List[int]) -> int:
    
    @lru_cache(None)
    def dfs(pos: int, hasLeadingZero: bool, isLimit: bool, has: bool) -> int:
        """当前在第pos位，hasLeadingZero表示有前导0，isLimit表示是否贴合上界, has表示是否出现过2、5、6、9"""
        if pos == len(nums):
            return not hasLeadingZero and has

        res = 0
        up = nums[pos] if isLimit else 9
        for cur in range(up + 1):
            if hasLeadingZero and cur == 0:
                res += dfs(pos + 1, True, (isLimit and cur == up), has or cur in {2, 5, 6, 9})
            else:
                if cur not in digits:
                    continue
                res += dfs(pos + 1, False, (isLimit and cur == up), has or cur in {2, 5, 6, 9})
        return res

    nums = list(map(int, str(upper)))
    return dfs(0, True, True, False)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return cal(n, [0, 1, 8, 2, 5, 6, 9])
```