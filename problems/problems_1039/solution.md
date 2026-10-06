# [C/Py/Java/Ts/Go] Dynamic programming

> Author: Benhao
> Date: 2023-04-02
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---

> Problem: [1039. 多边形三角剖分的最低得分](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/description/)

[TOC]

# Intuition
1. Every edge of the polygon eventually belongs to a triangle.
2. Choosing a triangle for an edge amounts to choosing its third vertex.
3. Choosing a triangle (its third vertex) splits the polygon into two minimum-triangulation subproblems: from the left endpoint to that vertex, and from that vertex to the right endpoint. Add the chosen triangle's score.

# Approach
> Interval dynamic programming

# Code
```Python3 []

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j] for k in range(i + 1, j)) if j - i >= 2 else 0
        
        return dfs(0, len(values) - 1)
```
```C []
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int minScoreTriangulation(int* values, int valuesSize){
    int **dp = (int **) malloc(sizeof(int *) * valuesSize);
    memset(dp, 0, sizeof(int *) * valuesSize);
    for (int i = 0; i < valuesSize; i++) {
        dp[i] = (int *) malloc(sizeof(int) * valuesSize);
        for (int j = 0; j < valuesSize; j++) {
            dp[i][j] = j - i < 2 ? 0 : 0x3fffff;
        }
    }
    for (int len = 2; len < valuesSize; len++) {
        for (int i = 0; i < valuesSize - len; i++) {
            int j = i + len;
            for (int k = i + 1; k < j; k++) {
                dp[i][j] = MIN(dp[i][j], values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]);
            }
        }
    }
    return dp[0][valuesSize - 1];
}
```
```Java []
class Solution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = j - i < 2 ? 0 : 0x3fffff;
            }
        }
        for (int len = 2; len < n; len++) {
            for (int i = 0; i < n - len; i++) {
                int j = i + len;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```
```TypeScript []
function minScoreTriangulation(values: number[]): number {
    const n: number = values.length
    const dp: Array<Array<number>> = new Array<Array<number>>(n)
    for (let i = 0; i < n; i++) {
        dp[i] = new Array<number>(n)
        for (let j = 0; j < n; j++) {
            dp[i][j] = j - i < 2 ? 0 : 0x3fffff
        }
    }
    for (let len = 2; len < n; len++) {
        for (let i = 0; i < n - len; i++) {
            const j: number = i + len
            for (let k = i + 1; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j], values[i] * values[k] * values[j] + dp[i][k] + dp[k][j])
            }
        }
    }
    return dp[0][n - 1]
};
```
```Go []
func minScoreTriangulation(values []int) int {
    n := len(values)
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n)
    }
    for len := 2; len < n; len++ {
        for i := 0; i < n - len; i++ {
            dp[i][i + len] = 0x3fffff
            for j, k := i + len, i + 1; k < j; k++ {
                dp[i][j] = min(dp[i][j], values[i] * values[k] * values[j] + dp[i][k] + dp[k][j])
            }
        }
    }
    return dp[0][n - 1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
