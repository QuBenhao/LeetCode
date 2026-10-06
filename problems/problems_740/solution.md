# [Python3/Go] House Robber dynamic programming

> Author: Benhao
> Date: 2021-05-04
> Upvotes: 6
> Tags: Go, Python, Python3

---

### Approach
First, use Counter and sorting to process the values in ascending order. For each `num`, checking whether the previous value is `num-1` is enough to determine the best score when taking it.
Use `max_so_far` for the current maximum and `max_except_last` for the maximum excluding the previous value.
When values are adjacent, written here as `num == num-1`, the best score from taking the current value is the maximum excluding the previous value plus the current contribution.
When they are not adjacent, the `else` case, add the current contribution to the current maximum.

Use dynamic programming to maintain the best scores for taking and skipping the current value.
### Code

```python3
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ns = sorted(cnt.keys())
        max_so_far = cnt[ns[0]] * ns[0]
        max_except_last = 0
        for i in range(1,len(cnt)):
            if ns[i-1] == ns[i] - 1:
                max_except_last, max_so_far = max_so_far, max(max_so_far, max_except_last + cnt[ns[i]] * ns[i])
            else:
                max_except_last,max_so_far = max_so_far, max_so_far + cnt[ns[i]] * ns[i]
        return max_so_far
```
```Python3 []
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts, m = Counter(nums), max(nums)
        dp0 = dp1 = 0
        for i in range(1, m + 1):
            dp0, dp1 = max(dp0, dp1), dp0 + cnts[i] * i
        return max(dp0, dp1)
```
```Go []
func deleteAndEarn(nums []int) int {
    cnts, m, dp0, dp1 := map[int]int{}, 0, 0, 0
    for _, num := range nums {
        cnts[num]++
        m = max(num, m)
    }
    for i := 1; i <= m; i++ {
        dp0, dp1 = max(dp0, dp1), dp0 + cnts[i] * i
    }
    return max(dp0, dp1)
}

func max(vals ...int) (ans int) {
    ans = vals[0]
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return
}

```
