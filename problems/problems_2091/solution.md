# [Python/Go] Direct simulation

> slug: pythongo-zhi-jie-mo-ni-by-himymben-g324
> date: 2021-11-28
> tags: Go, Python, Python3
> question: Removing Minimum and Maximum From Array (removing-minimum-and-maximum-from-array)
> url: https://leetcode.cn/problems/removing-minimum-and-maximum-from-array/solutions/yUCoR2/pythongo-zhi-jie-mo-ni-by-himymben-g324/

---
### Approach
Either delete from the left through the rightmost target,
delete from the right through the leftmost target,
or delete some elements from each end.

### Code

```Python3 []
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        imin, imax = 0, 0
        for i, num in enumerate(nums):
            if num > nums[imax]:
                imax = i
            if num < nums[imin]:
                imin = i
        return min(max(imin, imax) + 1, len(nums) - min(imin, imax), min(imin,imax) + 1 + len(nums) - max(imin, imax))
```
```Go []
func minimumDeletions(nums []int) int {
    imin, imax := 0, 0
    for i, num := range nums {
        if num < nums[imin] {
            imin = i
        }
        if num > nums[imax] {
            imax = i
        }
    }
    return min(min(max(imax, imin) + 1, len(nums) - min(imax, imin)), min(imax, imin) + 1 + len(nums) - max(imin, imax))
}

func min(a,b int) int {
    if a < b{
        return a
    }
    return b
}

func max(a,b int) int {
    if a > b{
        return a
    }
    return b
}
```

[@SanYeYYDS](/u/sanyeyyds/) 

```Python3
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        return min(max((imin:=nums.index(min(nums))), (imax:=nums.index(max(nums)))) + 1, (n:=len(nums))- min(imin, imax), min(imin,imax) + 1 + n - max(imin, imax))
```
