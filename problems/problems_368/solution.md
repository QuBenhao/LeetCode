# [Python] 字典dp

> Author: Benhao
> Date: 2021-04-22
> Upvotes: 5
> Tags: Python

---

### 解题思路
dp[i]代表对i来说最长的数组

### 代码

```python3
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = dict()
        ans = []
        for num in nums:
            max_list = []
            for key, val in dp.items():
                if num % key == 0 and len(val) > len(max_list):
                    max_list = val
            if not max_list:
                dp[num] = [num]
            else:
                dp[num] = max_list + [num]
            if len(dp[num]) > len(ans):
                ans = dp[num]
        return ans
```
或者写成这样，有整除的数中max(dp,key=len)，就用最大的结果的列表加上当前的值
没有就新建一个当前值的列表
```python3
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = dict()
        for num in nums:
            try:
                dp[num] = max([v for k,v in dp.items() if num % k == 0],key=len) + [num]
            except:
                dp[num] = [num]
        return max(dp.values(),key=len)
```