# [Python] 前缀和+hash

> Author: Benhao
> Date: 2021-07-07
> Upvotes: 13
> Tags: Python, Python3

---

### 解题思路
我们要找到全部的子数组和为goal,直觉上我们需要找到所有前缀和里的i和j,满足presum[j] - presum[i] == goal.
但是这样找i和j需要遍历两次，是o($n^2$)的。

故采取Counter存储前面的所有presum[i] == presum[j] - goal的个数，答案累加即可。
本题前缀和其实也是统计1的个数。

### 代码

```python3
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        countOnes = ans = 0
        cnts = Counter({0:1})
        for num in nums:
            countOnes += num
            ans += cnts[countOnes - goal]
            cnts[countOnes] += 1
        return ans
```