# [Python/Go] Dynamic programming

> slug: pythongo-dong-tai-gui-hua-by-himymben-8wh8
> date: 2022-02-07
> tags: Go, Python, Python3
> question: 秋叶收藏集 (UlBDOe)
> url: https://leetcode.cn/problems/UlBDOe/solutions/yhdRWu/pythongo-dong-tai-gui-hua-by-himymben-8wh8/

---
### Approach
At each position, track three states: only r, some r followed by some y, and some r followed by some y followed by some r. Three variables store the minimum operations needed for these states.

If the current character is r:
> r inherits the previous r state with no operation. (Initialize it to 0 at the first character.)
> ry must change the current `r` to `y`, costing 1 operation, and can follow the cheaper of the previous r and ry states.
> ryr needs no operation and follows the cheaper of the previous ry and ryr states.

If the current character is y:
> r must change `y` to `r`, costing 1 operation, and follows the previous r state. (Initialize it to 1 at the first character.)
> ry follows the cheaper of the previous r and ry states.
> ryr must change `y` to `r`, costing 1 operation, and follows the cheaper of the previous ry and ryr states.

### Code

```python3 []
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        r, ry, ryr = inf, inf, inf
        for c in leaves:
            if c == 'r':
                r, ry, ryr = 0 if r == inf else r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1 if r != inf else 1, min(r, ry), min(ry, ryr) + 1
        return ryr
```
```Go []
const inf int = 0x3f3f3f
func minimumOperations(leaves string) int {
    r, ry, ryr := inf, inf, inf
    for i := range leaves {
        if leaves[i] == 'r' {
            if i == 0 {
                r = 0
            } else {
                ry, ryr = min(r, ry) + 1, min(ry, ryr)
            }
        } else {
            if i == 0 {
                r = 1
            } else {
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr) + 1
            }
        }
    }
    return ryr
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
```
