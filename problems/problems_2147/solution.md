# [Python/Go] Simple combinatorial counting

> Author: Benhao
> Date: 2022-01-23
> Upvotes: 4
> Tags: Go, Python, Python3

---

### Approach
Count the available spaces between each consecutive pair of seat groups, with two seats per group.

### Code

```python3 []
MOD = 10**9 + 7
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans, cnts, last = 1, 0, 0
        for i, c in enumerate(corridor):
            if c == 'S':
                cnts += 1
                if cnts >= 3 and cnts % 2:
                    ans = (ans * (i - last)) % MOD
                last = i
        return 0 if not cnts or cnts % 2 else ans
```
```Golang []
const mod int = 1e9 + 7
func numberOfWays(corridor string) int {
    ans, cnts := 1, 0
    for i, last := 0, 0; i < len(corridor); i++ {
        if corridor[i] == 'S' {
            cnts += 1
            if cnts >= 3 && cnts % 2 == 1 {
                ans = (ans * (i - last)) % mod
            }
            last = i
        }
    }
    if cnts > 0 && cnts % 2 == 0 {
        return ans
    }
    return 0
}
```
