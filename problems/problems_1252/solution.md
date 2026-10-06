# [Python/Java/TypeScript/Go] Inclusion-exclusion

> slug: pythonjavatypescriptgo-rong-chi-yuan-li-7c5n1
> date: 2022-07-12
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Cells with Odd Values in a Matrix (cells-with-odd-values-in-a-matrix)
> url: https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/solutions/HQ9rOt/pythonjavatypescriptgo-rong-chi-yuan-li-7c5n1/

---
### Approach
Count which rows and columns were incremented an odd number of times. Any even number of increments is equivalent to 0 for parity, so it can be treated as no change.
Use inclusion-exclusion on these rows and columns to calculate the result.

Specifically:
Each row contributes n odd numbers and each column contributes m odd numbers, but every intersection of such a row and column is even and does not qualify.
Each intersection has been counted twice, so subtract both contributions.

### Code

```Python3 []
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        return (r := sum(rows)) * n + (c := sum(cols)) * m - 2 * r * c
```
```Java []
class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[] rows = new int[m];
        int[] cols = new int[n];
        for (int[] indice: indices) {
            rows[indice[0]] ^= 1;
            cols[indice[1]] ^= 1;
        }
        int r = 0, c = 0;
        for (int i = 0; i < m; i++) {
            r += rows[i];
        }
        for (int i = 0; i < n; i++) {
            c += cols[i];
        }
        return r * n + c * m - 2 * r * c;
    }
}
```
```TypeScript []
function oddCells(m: number, n: number, indices: number[][]): number {
    const rows = new Array<number>(m).fill(0), cols = new Array<number>(n).fill(0)
    for (const [r, c] of indices) {
        rows[r] ^= 1
        cols[c] ^= 1
    }
    const r = rows.reduce((a, b) => a + b), c = cols.reduce((a, b) => a + b)
    return r * n + c * m - 2 * r * c
};
```
```Go []
func oddCells(m int, n int, indices [][]int) int {
    rows, cols := make([]int, m), make([]int, n)
    for _, indice := range indices {
        rows[indice[0]] ^= 1
        cols[indice[1]] ^= 1
    }
    r, c := sum(rows), sum(cols)
    return r * n + c * m - 2 * r * c
}

func sum(arr []int) (s int) {
    for _, num := range arr {
        s += num
    }
    return
}
```
