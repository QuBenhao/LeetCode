# [Python/Go] 模拟

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 1
> Tags: Go, Python, Python3

---

```Python3 []
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i] == nums[j] and not i * j % k for i in range(len(nums)) for j in range(i + 1, len(nums)))
```
```Go []
func countPairs(nums []int, k int) (ans int) {
    for i, num := range nums {
        for j := i + 1; j < len(nums); j++ {
            if num == nums[j] && i * j % k == 0 {
                ans++
            }
        }
    }
    return
}
```