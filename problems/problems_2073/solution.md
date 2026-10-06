# [Go/Python] Transform the problem into a sum

> Author: Benhao
> Date: 2021-11-14
> Upvotes: 5
> Tags: Go, Python, Python3

---

### Approach
Contributions from people ahead are limited by the value at k;
contributions from people behind are limited by the value at k minus 1.

### Code
```Python3 []
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(t, tickets[k]) if i <= k else min(t, tickets[k]-1)  for i,t in enumerate(tickets))
```
```golang []
func timeRequiredToBuy(tickets []int, k int) int {
    ans := 0
    for i, v := range tickets {
        if i <= k {
            if v < tickets[k]{
                ans += v
            }else {
                ans += tickets[k]
            }
        } else {
            if v < tickets[k] - 1{
                ans += v
            } else {
                ans += tickets[k] - 1
            }
        }
    }
    return ans
}
```
