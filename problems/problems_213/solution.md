# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-08
> Upvotes: 2
> Tags: Go, Python, Python3

---

### Approach
Consider the cases of taking and skipping the first house; each becomes the same as House Robber I.

### Code

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
