# [Python] 根据数据范围要按nums遍历，不能按lower到upper

> slug: python-gen-ju-shu-ju-fan-wei-yao-an-nums-zt62
> date: 2021-08-21
> tags: Python, Python3
> question: Missing Ranges (missing-ranges)
> url: https://leetcode.cn/problems/missing-ranges/solutions/Ua5erp/python-gen-ju-shu-ju-fan-wei-yao-an-nums-zt62/

---
```python3
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # 添加终止边界
        nums.append(upper + 1)
        ans = []
        last = lower - 1
        for num in nums:
            # 比上一个数字中有缺失,需要添加在答案中的
            if num - last > 2:
                ans.append(str(last+1) + '->' + str(num-1))
            elif num - last == 2:
                ans.append(str(last+1))
            last = num
        return ans

```

20240622题目已改变
```python3 [方法一]
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # 添加终止边界
        nums.append(upper + 1)
        ans = []
        last = lower - 1
        for num in nums:
            # 比上一个数字中有缺失,需要添加在答案中的
            if num - last > 2:
                ans.append([last + 1, num - 1])
            elif num - last == 2:
                ans.append([last + 1, last + 1])
            last = num
        return ans
```
```Python3 [方法二]
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