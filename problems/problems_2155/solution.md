# [Python/Go] Prefix sums

> slug: pythongo-qian-zhui-he-by-himymben-2fnr
> date: 2022-01-30
> tags: Go, Python, Python3
> question: All Divisions With the Highest Score of a Binary Array (all-divisions-with-the-highest-score-of-a-binary-array)
> url: https://leetcode.cn/problems/all-divisions-with-the-highest-score-of-a-binary-array/solutions/YfYrMr/pythongo-qian-zhui-he-by-himymben-2fnr/

---
### Approach
Precompute counts of ones or zeros, evaluate the answer at each position, and update the maximum.
The simplified comparison formula is `f[i] = presum[i] * 2 - i`.

### Code

```Python3 []
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        presum, m, ans = 0, -inf, []
        for i in range(n+1):
            if (res:= presum * 2 - i) > m:
                m = res
                ans = [i]
            elif res == m:
                ans.append(i)
            if i < n:
                presum += nums[i] == 0
        return ans
```
```Golang []
func maxScoreIndices(nums []int) []int {
    n := len(nums)
    presum, m, ans := 0, -1-n, []int{}
    for i := 0; i <= n; i++ {
        if cur := presum * 2 - i; cur > m {
            m, ans = cur, []int{i}
        } else if cur == m {
            ans = append(ans, i)
        }
        if i < n && nums[i] == 0{
            presum++
        }
    }
    return ans
}
```
