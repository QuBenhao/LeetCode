# [Python3/Go] 打家劫舍动态规划

> Author: Benhao
> Date: 2021-05-04
> Upvotes: 6
> Tags: Go, Python, Python3

---

### 解题思路
首先想到用Counter和排序处理数据，这样从小到大看的话，`num`只需要考虑前一个是不是`num-1`，就可以判断当前元素可以取得的最大值了。
使用`max_so_far`来记录当前最大值，`max_except_last`来记录上个最大值。
这样在出现相邻的情况时,也就是`num == num-1`，当前能取的最大值就是上个最大值加上当前值；
在不出现相邻的情况时，也就是`else`, 当前能取的最大值就是当前最大值加上当前值；

动态规划，维护一个选当前和不选当前的最大得分。
### 代码

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