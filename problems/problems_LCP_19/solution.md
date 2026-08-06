# [Python/Go] 动态规划

> slug: pythongo-dong-tai-gui-hua-by-himymben-8wh8
> date: 2022-02-07
> tags: Go, Python, Python3
> question: 秋叶收藏集 (UlBDOe)
> url: https://leetcode.cn/problems/UlBDOe/solutions/yhdRWu/pythongo-dong-tai-gui-hua-by-himymben-8wh8/

---
### 解题思路
维护到任意位置我们有三种状态，全是r、若干r若干y、若干r若干y若干r，我们用三个变量维护维持这三种状态的最小操作数。

若当前字符为r：
> r 继承之前的r，不需要操作。（如果是第一次，初始化为0）
> ry 必须将当前`r`变成`y`，操作为1，可以从之前的r和ry之中更小的得到
> ryr 不需要操作，从之前的ry和ryr之中更小的得到

若当前字符为y:
> r 必须将`y`变成`r`，操作为1。从之前的r得到（如果是第一次，初始化为1）
> ry  可以从之前的r和ry之中更小的得到
> ryr 必须将`y`变成`r`，操作为1。从之前ry和ryr之中更小的得到

### 代码

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