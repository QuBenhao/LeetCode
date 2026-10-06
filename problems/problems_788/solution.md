# [Python] Digit DP template

> Author: Benhao
> Date: 2022-09-25
> Upvotes: 10
> Tags: Python, Python3

---

### Approach
I learned this some time ago from [草莓奶昔](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/python-shu-wei-dpmo-ban-ti-by-981377660l-xtkb/)

### Code

```python3
def cal(upper: int, digits: List[int]) -> int:
    
    @lru_cache(None)
    def dfs(pos: int, hasLeadingZero: bool, isLimit: bool, has: bool) -> int:
        """At position pos, hasLeadingZero indicates leading zeros, isLimit indicates whether the upper bound still applies, and has indicates whether 2, 5, 6, or 9 has appeared"""
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
