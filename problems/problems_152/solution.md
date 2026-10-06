# [Python/Go] Maintain the maximum and minimum subarray products

> Author: Benhao
> Date: 2022-02-12
> Upvotes: 2
> Tags: Go, Python, Python3

---

### Approach
Because negative numbers are allowed, the maximum may come from multiplying the previous minimum by the current negative number.

### Code

```Python3 []
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max, pre_min, ans = 1, 1, -inf
        for num in nums:
            pre_max, pre_min = max(pre_max * num, pre_min * num, num), min(pre_max * num, pre_min * num, num)
            ans = max(ans, pre_max)
        return ans
```
```Go []
const inf int = 0x3f3f3f
func maxProduct(nums []int) int {
    preMax, preMin, ans := 1, 1, -inf
    for _, num := range nums {
        preMax, preMin = max(preMax * num, preMin * num, num), min(preMax * num, preMin * num, num)
        ans = max(preMax, ans)
    }
    return ans
}

func max(vals ...int) int {
    ans := -inf
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return ans
}

func min(vals ...int) int {
    ans := inf
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
} 
```
