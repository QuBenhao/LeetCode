# [Python/Java/JavaScript/Go] 前缀和模拟

> Author: Benhao
> Date: 2022-03-23
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
由于本题平滑器大小固定为3*3，所以暴力遍历统计和前缀和优化统计都能过。

### 代码

```python3
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        return [[sum(img[di][dj] if 0 <= di < m and 0 <= dj < n else 0 for dj in range(j - 1, j + 2) for di in range(i - 1, i + 2)) // sum(0 <= di < m and 0 <= dj < n for dj in range(j - 1, j + 2) for di in range(i - 1, i + 2)) for j in range(n)] for i in range(m)] if (m := len(img)) and (n := len(img[0])) else [[]]
```

```Python3 []
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + img[i][j]
        return [[(presum[(mxi := min(m, i + 2))][(mxj := min(n, j + 2))] - presum[(mii := max(0, i - 1))][mxj] - presum[mxi][(mij := max(0, j - 1))] + presum[mii][mij]) // ((mxi - mii) * (mxj - mij)) for j in range(n)] for i in range(m)]
```
```Java []
class Solution {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length, n = img[0].length;
        int[][] presum = new int[m + 1][n + 1], ans = new int[m][n];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                presum[i + 1][j + 1] = presum[i][j + 1] + presum[i + 1][j] - presum[i][j] + img[i][j];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++) {
                int cnts = 0, downI = Math.max(0, i - 1), upI = Math.min(m, i + 2), downJ = Math.max(0, j - 1), upJ = Math.min(n, j + 2);
                for(int di = downI; di < upI; di++)
                    for(int dj = downJ; dj < upJ; dj++)
                        cnts++;
                ans[i][j] = (presum[upI][upJ] - presum[upI][downJ] - presum[downI][upJ] + presum[downI][downJ]) / cnts;
            }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} img
 * @return {number[][]}
 */
var imageSmoother = function(img) {
    const m = img.length, n = img[0].length, presum = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0)), ans = new Array(m).fill(0).map(() => new Array(n).fill(0))
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + img[i][j]
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++) {
            const di = Math.max(0, i - 1), ui = Math.min(m, i + 2), dj = Math.max(0, j - 1), uj = Math.min(n, j + 2)
            ans[i][j] = Math.floor((presum[ui][uj] - presum[ui][dj] - presum[di][uj] + presum[di][dj])/((ui - di) * (uj - dj)))
        }
    return ans
};
```
```Go []
func imageSmoother(img [][]int) [][]int {
    m, n := len(img), len(img[0])
    presum, ans := make([][]int, m + 1), make([][]int, m)
    presum[0] = make([]int , n + 1)
    for i := 0; i < m; i++ {
        presum[i + 1] = make([]int, n + 1)
        ans[i] = make([]int, n)
        for j := 0; j < n; j++ {
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + img[i][j]
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            di, ui, dj, uj := max(0, i - 1), min(m, i + 2), max(0, j - 1), min(n, j + 2)
            ans[i][j] = (presum[ui][uj] - presum[ui][dj] - presum[di][uj] + presum[di][dj]) / ((ui - di) * (uj - dj))
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