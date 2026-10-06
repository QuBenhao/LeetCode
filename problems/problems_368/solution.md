# [Python] Dictionary-based DP

> Author: Benhao
> Date: 2021-04-22
> Upvotes: 5
> Tags: Python

---

### Approach
dp[i] represents the longest array for i.

### Code

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
Alternatively, among divisible predecessors, take max(dp,key=len) and append the current value to the longest result.
If none exists, create a list containing only the current value.
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
