# [Python/Go] Enumerate bitmasks and simulate

> slug: pythongo-er-jin-zhi-mei-ju-mo-ni-by-himy-x43g
> date: 2022-01-23
> tags: Python, Python3
> question: Maximum Good People Based on Statements (maximum-good-people-based-on-statements)
> url: https://leetcode.cn/problems/maximum-good-people-based-on-statements/solutions/1Ix3ui/pythongo-er-jin-zhi-mei-ju-mo-ni-by-himy-x43g/

---
### Approach
Enumerate all possible sets of good people and check whether each assignment is consistent. Update the maximum for valid assignments; invalid ones cannot be answers.

### Code

```python3 []
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def check(i):
            ans = 0
            for j in range(len(statements)):
                if (i >> j) & 1:
                    if any(s != (i >> k) & 1 for k, s in enumerate(statements[j]) if s < 2):
                        return 0
                    ans += 1
            return ans

        return max(check(i) for i in range(1 << len(statements)))
```
```Go []
func maximumGood(statements [][]int) (ans int) {
    next:
    for i, n := 1, len(statements); i < 1 << n; i++ {
        cnts := 0
        for j := 0; j < n; j++{
            if (i >> j) & 1 != 0 {
                for k, s := range statements[j] {
                    if s < 2 && (i >> k) & 1 != s{
                        continue next
                    }
                }
                cnts++
            }
        }
        if cnts > ans {
            ans = cnts
        }
    } 
    return
}
```
