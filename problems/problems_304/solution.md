# [Python/Go] 二维前缀和应用题

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
本题为二维矩阵前缀和模板题

### 代码

```Python3 []
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.presum[i][j] = self.presum[i - 1][j] + self.presum[i][j - 1] - self.presum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] - self.presum[row1][col2 + 1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```
```Go []
type NumMatrix struct {
    presum [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    m, n := len(matrix), len(matrix[0])
    presum := make([][]int, m + 1)
    presum[0] = make([]int, n + 1)
    for i := 1; i <= m; i++ {
        presum[i] = make([]int, n + 1)
        for j := 1; j <= n; j++ {
            presum[i][j] = presum[i][j - 1] + presum[i - 1][j] - presum[i - 1][j - 1] + matrix[i - 1][j - 1]
        }
    }
    return NumMatrix{presum}
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.presum[row2 + 1][col2 + 1] - this.presum[row2 + 1][col1] - this.presum[row1][col2 + 1] + this.presum[row1][col1]
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
```