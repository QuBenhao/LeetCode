# [Go/Python] 转换求和

> Author: Benhao
> Date: 2021-11-14
> Upvotes: 5
> Tags: Go, Python, Python3

---

### 解题思路
前面的影响以k的值为下限，
后面的影响以k的值-1为下限。

### 代码
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