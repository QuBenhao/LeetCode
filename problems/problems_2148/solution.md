# [Python/Go] Simulation

> slug: pythongo-mo-ni-by-himymben-tl7t
> date: 2022-01-23
> tags: Go, Python, Python3
> question: Count Elements With Strictly Smaller and Greater Elements  (count-elements-with-strictly-smaller-and-greater-elements)
> url: https://leetcode.cn/problems/count-elements-with-strictly-smaller-and-greater-elements/solutions/p1VlE0/pythongo-mo-ni-by-himymben-tl7t/

---
### Approach
The maximum and minimum values cannot satisfy the conditions, while every other value can use them to do so. Count the occurrences of the maximum and minimum.

### Code

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
