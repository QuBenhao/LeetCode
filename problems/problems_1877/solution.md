# [Python/Go] 贪心

> Author: Benhao
> Date: 2021-07-19
> Upvotes: 5
> Tags: Go, Python, Python3

---

### 解题思路
田忌赛马。
为了使得最大的数的和尽可能地小，要将它和最小的值匹配。

### 代码

```python3
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n - 1 -i] for i in range(n >> 1))
```

```golang
func minPairSum(nums []int) (ans int) {
    sort.Ints(nums)
    n := len(nums)
    for i:=0; i < n/2; i++ {
        ans = max(ans, nums[i]+nums[n-1-i])
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```