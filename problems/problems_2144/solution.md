# [Python/Go] Sort and simulate greedily

> slug: pythongo-pai-xu-tan-xin-mo-ni-by-himymbe-az3r
> date: 2022-01-23
> tags: Go, Python, Python3
> question: Minimum Cost of Buying Candies With Discount (minimum-cost-of-buying-candies-with-discount)
> url: https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/solutions/SPXj1s/pythongo-pai-xu-tan-xin-mo-ni-by-himymbe-az3r/

---
### Approach
Sort in descending order. The two most expensive candies cannot be free, but pairing them lets us receive the most valuable possible free candy: the third most expensive.

### Code

```python3 []
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(c for i, c in enumerate(sorted(cost, reverse=True)) if i % 3 < 2)
```
```golang []
func minimumCost(cost []int) (ans int) {
    sort.Ints(cost)
    for i, n := 0, len(cost); i < n; i++ {
        if i % 3 < 2 {
            ans += cost[n - 1 - i]
        }
    }
    return 
}
```
