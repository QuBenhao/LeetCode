# [Python/Go] 二维数组前缀和

> slug: pythongo-er-wei-shu-zu-qian-zhui-he-by-h-risi
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Matrix Block Sum (matrix-block-sum)
> url: https://leetcode.cn/problems/matrix-block-sum/solutions/34e3L0/pythongo-er-wei-shu-zu-qian-zhui-he-by-h-risi/

---
### 解题思路
预处理二维前缀和，可以o(1)求出每个点的周围k个正方形的大小。

### 代码

```Python3 []
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + mat[i - 1][j - 1]
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = presum[(ri := min(m, i + k + 1))][(rj := min(n, j + k + 1))] - presum[ri][(lj := max(0, j - k))] - presum[(li := max(0, i - k))][rj] + presum[li][lj]
        return res
```
```Go []
func matrixBlockSum(mat [][]int, k int) [][]int {
    m, n := len(mat), len(mat[0])
    presum := make([][]int, m + 1)
    ans := make([][]int, m)
    presum[0] = make([]int, n + 1)
    for i := 1; i <= m; i++ {
        presum[i] = make([]int, n + 1)
        ans[i - 1] = make([]int, n)
        for j := 1; j <= n; j++ {
            presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + mat[i - 1][j - 1]
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            li, lj, ri, rj := max(i - k, 0), max(j - k, 0), min(m, i + k + 1), min(n, j + k + 1)
            ans[i][j] = presum[ri][rj] - presum[li][rj] - presum[ri][lj] + presum[li][lj]
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```