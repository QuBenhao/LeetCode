# [Python/Go] 前缀和 or 不用前缀和的定长滑窗

> slug: pythongo-qian-zhui-he-or-bu-yong-qian-zh-fra1
> date: 2021-11-28
> tags: Go, Python, Python3
> question: K Radius Subarray Averages (k-radius-subarray-averages)
> url: https://leetcode.cn/problems/k-radius-subarray-averages/solutions/hQWRcw/pythongo-qian-zhui-he-or-bu-yong-qian-zh-fra1/

---
### 解题思路
两种模拟方式

### 代码

```python3 []
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        presum = [0] + list(accumulate(nums))
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                ans[i] = (presum[i + k + 1] - presum[i-k])//(2*k + 1)
        return ans
```
```go []
func getAverages(nums []int, k int) []int {
    n := len(nums)
    ans := make([]int, n)
    sum := 0
    i := 0
    for ; i < n && i <= 2 * k; i++ {
        ans[i] = -1
        sum += nums[i]
    }
    for ; i <= n; i++ {
        if i - 1 - 2 * k >= 0{
            ans[i-1-k] = sum / (2 * k + 1)
        }
        if i == n {
            break
        }
        ans[i] = -1
        sum += nums[i] - nums[i-1-2*k]
    }
    return ans
}
```