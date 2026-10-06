# [Python/Go] Enumeration

> slug: pythongo-mei-ju-by-himymben-vzx8
> date: 2022-02-13
> tags: Go, Python, Python3
> question: Removing Minimum Number of Magic Beans (removing-minimum-number-of-magic-beans)
> url: https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/solutions/8nx8J4/pythongo-mei-ju-by-himymben-vzx8/

---
### Approach
Enumerate possible final bean counts and choose the one that leaves the most beans in total (and therefore removes the fewest).

### Code

```Python3 []
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        cnts, ans, vals, s, n = Counter(beans), 0, 0, sum(beans), len(beans)
        for b in sorted(cnts.keys()):
            ans = max(ans, b * (n - vals))
            vals += cnts[b]
        return s - ans
```
```Go []
func minimumRemoval(beans []int) int64 {
    sort.Ints(beans)
    s, max, n := 0, 0, len(beans)
    for i, b := range beans {
        s += b
        if v := b * (n - i); v > max {
            max = v
        }
    }
    return int64(s - max)
}
```
