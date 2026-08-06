# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-5s3b
> date: 2021-11-28
> tags: Go, Python, Python3
> question: Find Target Indices After Sorting Array (find-target-indices-after-sorting-array)
> url: https://leetcode.cn/problems/find-target-indices-after-sorting-array/solutions/HiIyPE/pythongo-mo-ni-by-himymben-5s3b/

---
### 代码

```golang []
func targetIndices(nums []int, target int) (ans []int) {
    sort.Sort(sort.IntSlice(nums))
    for i := 0; i < len(nums); i++ {
        if nums[i] == target {
            ans = append(ans, i)
        } else if nums[i] > target {
            break
        }
    }
    return ans
}
```
```python3 []
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]
```