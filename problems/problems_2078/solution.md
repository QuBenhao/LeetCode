# [Python/Go] 暴力

> slug: pythongo-bao-li-by-himymben-7uje
> date: 2021-11-21
> tags: Go, Python, Python3
> question: Two Furthest Houses With Different Colors (two-furthest-houses-with-different-colors)
> url: https://leetcode.cn/problems/two-furthest-houses-with-different-colors/solutions/Erpwui/pythongo-bao-li-by-himymben-7uje/

---
### 代码

```python3 []
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i, c in enumerate(colors):
            for j in range(i + 1, len(colors)):
                if colors[j] != c:
                    ans = max(ans, abs(j - i))
        return ans
```
```go []
func maxDistance(colors []int) int {
    ans := 0
    for i, v := range colors {
        for j := i + 1; j < len(colors); j++ {
            if colors[j] != v {
                if j - i > ans {
                    ans = j - i
                }
            }
        }
    }
    return ans
}
```