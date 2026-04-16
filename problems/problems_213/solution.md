# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-08
> Upvotes: 2
> Tags: Go, Python, Python3

---

### 解题思路
讨论一下取第一个和不取第一个，和打家劫舍I就没有区别了

### 代码

```Python3 []
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0 = rob1 = nrob0 = nrob1 = 0
        for i in range(len(nums) - 1):
            rob0, rob1 = rob1 + nums[i], max(rob0, rob1)
            nrob0, nrob1 = nrob1 + nums[i + 1], max(nrob0, nrob1)
        return max(nums[0], rob0, rob1, nrob0, nrob1)
```
```Go []
func rob(nums []int) int {
    rob0, rob1, nrob0, nrob1 := 0, 0, 0, 0
    for i := 0; i < len(nums) - 1; i++ {
        rob0, rob1 = rob1 + nums[i], max(rob0, rob1)
        nrob0, nrob1 = nrob1 + nums[i + 1], max(nrob0, nrob1)
    }
    return max(nums[0], rob0, rob1, nrob0, nrob1)
}

func max(vals ...int) (ans int) {
    for _, v := range vals {
        if v > ans {
            ans = v
        }
    }
    return
}
```