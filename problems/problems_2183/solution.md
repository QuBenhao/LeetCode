# [Python/Go] 动态规划 

> slug: pythongo-dong-tai-gui-hua-by-himymben-og2b
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Count Array Pairs Divisible by K (count-array-pairs-divisible-by-k)
> url: https://leetcode.cn/problems/count-array-pairs-divisible-by-k/solutions/wnuTtN/pythongo-dong-tai-gui-hua-by-himymben-og2b/

---
### 解题思路
蛮暴力的。可能因为k的最大因数个数是常数级别的所以还可以。

当前能加入答案的个数由之前所有最大公因数中乘是k的倍数的个数得到，再将当前最大公因数个数加入到统计。

### 代码

```Python3 []
class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        cnts, ans = Counter(), 0
        for num in nums:
            g = gcd(num, k)
            for c in cnts:
                if not (c * g) % k:
                    ans += cnts[c]
            cnts[g] += 1
        return ans
```
```Go []
func coutPairs(nums []int, k int) (ans int64) {
    cnts := map[int]int{}
    for _, num := range nums {
        g := gcd(num, k)
        for key, val := range cnts {
            if g * key % k == 0 {
                ans += int64(val)
            }
        }
        cnts[g] += 1
    }
    return
}

// 辗转相除法
func gcd(a, b int) int {
	for a != 0 {
		a, b = b % a, a
	}
	return b
}
```