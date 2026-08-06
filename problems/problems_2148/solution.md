# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-tl7t
> date: 2022-01-23
> tags: Go, Python, Python3
> question: Count Elements With Strictly Smaller and Greater Elements  (count-elements-with-strictly-smaller-and-greater-elements)
> url: https://leetcode.cn/problems/count-elements-with-strictly-smaller-and-greater-elements/solutions/p1VlE0/pythongo-mo-ni-by-himymben-tl7t/

---
### 解题思路
因为最大值、最小值一定不满足题目条件，而其他数字均可以用最大值和最小值满足条件，所以统计最大值、最小值的个数即可

### 代码

```python3 []
class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len(nums) - (cnts := Counter(nums))[mx] - cnts[mn] if (mx := max(nums)) != (mn := min(nums)) else 0
```
```go []
func countElements(nums []int) int {
    mx, mn, mxc, mnc := -100001, 100001, 0, 0
    for _, num := range nums {
        if num < mn {
            mn, mnc = num, 1
        } else if num == mn {
            mnc++
        }
        if num > mx {
            mx, mxc = num, 1
        } else if num == mx {
            mxc++
        }
    }
    if mn == mx {
        return 0
    }
    return len(nums) - mxc - mnc
}
```