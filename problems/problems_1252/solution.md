# [Python/Java/TypeScript/Go] 容斥原理

> slug: pythonjavatypescriptgo-rong-chi-yuan-li-7c5n1
> date: 2022-07-12
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Cells with Odd Values in a Matrix (cells-with-odd-values-in-a-matrix)
> url: https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/solutions/HQ9rOt/pythonjavatypescriptgo-rong-chi-yuan-li-7c5n1/

---
### 解题思路
我们只需要统计哪些行加了奇数次，哪些列加了奇数次 （因为所有偶数次的变化可以认为和0等价，相当于没变）
根据这些行和列，利用容斥原理计算最终结果。

具体是：
每一行会有n个数变为奇数，每一列会有m个数变为奇数，但是每一个行和列的交点都是偶数(不满足题意)，
却被计算了两次，所以要刨除掉所有交点的次数。

### 代码

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