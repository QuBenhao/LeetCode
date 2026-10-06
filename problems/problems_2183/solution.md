# [Python/Go] Dynamic programming

> slug: pythongo-dong-tai-gui-hua-by-himymben-og2b
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Count Array Pairs Divisible by K (count-array-pairs-divisible-by-k)
> url: https://leetcode.cn/problems/count-array-pairs-divisible-by-k/solutions/wnuTtN/pythongo-dong-tai-gui-hua-by-himymben-og2b/

---
### Approach
This is fairly brute force. It may be acceptable because the maximum number of divisors of k is bounded by a small constant.

Count previous greatest common divisors whose product with the current one is a multiple of k, add their counts to the answer, then record the current greatest common divisor.

### Code

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

// Euclidean algorithm
func gcd(a, b int) int {
	for a != 0 {
		a, b = b % a, a
	}
	return b
}
```
