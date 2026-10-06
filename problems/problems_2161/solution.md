# [Python] Two-pointer simulation

> slug: python-shuang-zhi-zhen-mo-ni-by-himymben-62d5
> date: 2022-02-06
> tags: Python, Python3
> question: Partition Array According to Given Pivot (partition-array-according-to-given-pivot)
> url: https://leetcode.cn/problems/partition-array-according-to-given-pivot/solutions/J2DFhv/python-shuang-zhi-zhen-mo-ni-by-himymben-62d5/

---
### Approach
Use the left pointer for values smaller than the pivot and the right pointer for larger values, then reverse the right side.

### Code

```python3
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot] * (n:=len(nums))
        l, r = 0, n - 1
        for num in nums:
            if num < pivot:
                ans[l] = num
                l += 1
            elif num > pivot:
                ans[r] = num
                r -= 1
        return ans[:r+1] + ans[r+1:][::-1]
```
