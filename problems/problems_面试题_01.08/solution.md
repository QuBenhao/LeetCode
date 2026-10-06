# [Python/Java/TypeScript/Go] Simulation

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-j72n
> date: 2022-09-30
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Zero Matrix LCCI (zero-matrix-lcci)
> url: https://leetcode.cn/problems/zero-matrix-lcci/solutions/ivOdFN/pythonjavatypescriptgo-mo-ni-by-himymben-j72n/

---
### Approach
This feels like a problem I have already solved on the main site.
First record whether the first row and column must eventually become zero. Then use that row and column to mark which remaining rows and columns must become zero.

### Code

```Python3 []
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row, first_col = any(not v for v in matrix[0]), any(not matrix[i][0] for i in range(m))
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            if not matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if not matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
```
```Java []
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRow = false, firstCol = false;
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRow = true;
                break;
            }
        }
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstCol = true;
                break;
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int j = 1; j < n; j++) {
            if (matrix[0][j] == 0) {
                for (int i = 1; i < m; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRow) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
        if (firstCol) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```
```TypeScript []
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const m: number = matrix.length, n: number = matrix[0].length
    let firstRow: boolean = false, firstCol: boolean = false
    for (let i = 0; i < m; i++) {
        if (matrix[i][0] == 0) {
            firstCol = true
            break
        }
    }
    for (let j = 0; j < n; j++) {
        if (matrix[0][j] == 0) {
            firstRow = true
            break
        }
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = matrix[0][j] = 0
            }
        }
    }
    for (let i = 1; i < m; i++) {
        if (matrix[i][0] == 0) {
            for (let j = 1; j < n; j++) {
                matrix[i][j] = 0
            }
        }
    }
    for (let j = 1; j < n; j++) {
        if (matrix[0][j] == 0) {
            for (let i = 1; i < m; i++) {
                matrix[i][j] = 0
            }
        }
    }
    if (firstRow) {
        for (let j = 0; j < n; j++) {
            matrix[0][j] = 0
        }
    }
    if (firstCol) {
        for (let i = 0; i < m; i++) {
            matrix[i][0] = 0
        }
    }
};
```
```Go []
func setZeroes(matrix [][]int)  {
    m, n, fr, fc := len(matrix), len(matrix[0]), false, false
    for i := 0; i < m; i++ {
        if matrix[i][0] == 0 {
            fc = true
            break
        }
    }
    for j := 0; j < n; j++ {
        if matrix[0][j] == 0 {
            fr = true
            break
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if matrix[i][j] == 0 {
                matrix[i][0], matrix[0][j] = 0, 0
            }
        }
    }
    for i := 1; i < m; i++ {
        if matrix[i][0] == 0 {
            for j := 1; j < n; j++ {
                matrix[i][j] = 0
            }
        }
    }
    for j := 1; j < n; j++ {
        if matrix[0][j] == 0 {
            for i := 1; i < m; i++ {
                matrix[i][j] = 0
            }
        }
    }
    if fr {
        for j := 0; j < n; j++ {
            matrix[0][j] = 0
        }
    }
    if fc {
        for i := 0; i < m; i++ {
            matrix[i][0] = 0
        }
    }
}
```
