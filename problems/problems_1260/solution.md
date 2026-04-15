# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-07-19
> Upvotes: 31
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
想象扁平化后的一维数组的平移，再将一维数组映射回二维。
具体来说:
原来的$(i, j)$对应的一维坐标为$i * n + j$,
向右平移$k$后为$i * n + j + k$,
总共只有$m * n$个位置所以最终坐标为$(i * n + j + k)$ % $(m * n)$,
转换回二维坐标即可。

### 代码

```Python3 []
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x, y = divmod(i * n + j + k, n)
                ans[x % m][y] = grid[i][j]
        return ans
```
```Java []
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][] ans = new int[m][n];
        for (int i = 0, total = m * n; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int nxt = (i * n + j + k) % total;
                ans[nxt / n][nxt % n] = grid[i][j];
            }
        }
        List<List<Integer>> res = new ArrayList<>(m);
        for (int i = 0; i < m; i++) {
            List<Integer> cur = new ArrayList<>(n);
            for (int j = 0; j < n; j++) {
                cur.add(ans[i][j]);
            }
            res.add(cur);
        }
        return res;
    }
}
```
```TypeScript []
function shiftGrid(grid: number[][], k: number): number[][] {
    const m: number = grid.length, n: number = grid[0].length
    const ans: number[][] = new Array<Array<number>>(m).fill(null).map(() => new Array<number>(n).fill(0)), total = m * n
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const nxt = (i * n + j + k) % total
            ans[Math.floor(nxt / n)][nxt % n] = grid[i][j]
        }
    }
    return ans
};
```
```Go []
func shiftGrid(grid [][]int, k int) [][]int {
    m, n := len(grid), len(grid[0])
    ans := make([][]int, m)
    for i := 0; i < m; i++ {
        ans[i] = make([]int, n)
    }
    for i, total := 0, m * n; i < m; i++ {
        for j := 0; j < n; j++ {
            nxt := (i * n + j + k) % total
            ans[nxt / n][nxt % n] = grid[i][j]
        }
    }
    return ans
}
```