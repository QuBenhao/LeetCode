# [Python] The constraints require traversing nums, not the range from lower to upper

> slug: python-gen-ju-shu-ju-fan-wei-yao-an-nums-zt62
> date: 2021-08-21
> tags: Python, Python3
> question: Missing Ranges (missing-ranges)
> url: https://leetcode.cn/problems/missing-ranges/solutions/Ua5erp/python-gen-ju-shu-ju-fan-wei-yao-an-nums-zt62/

---
```python3
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # Add a terminal boundary
        nums.append(upper + 1)
        ans = []
        last = lower - 1
        for num in nums:
            # Add the gap after the previous number to the answer
            if num - last > 2:
                ans.append(str(last+1) + '->' + str(num-1))
            elif num - last == 2:
                ans.append(str(last+1))
            last = num
        return ans

```

20240622: The problem has changed
```python3 [Approach 1]
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # Add a terminal boundary
        nums.append(upper + 1)
        ans = []
        last = lower - 1
        for num in nums:
            # Add the gap after the previous number to the answer
            if num - last > 2:
                ans.append([last + 1, num - 1])
            elif num - last == 2:
                ans.append([last + 1, last + 1])
            last = num
        return ans
```
```Python3 [Approach 2]
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = [[lower, upper]]
        for num in nums:
            if ans[-1][0] < num:
                ans[-1][1] = num - 1
                ans.append([num + 1, upper])
            elif ans[-1][0] == num:
                ans[-1][0] += 1
            else:
                break
            if ans[-1][0] > ans[-1][1]:
                ans.pop()
        return ans
```
