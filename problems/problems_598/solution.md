# [Python/Java/JavaScript/Go] 看成线性的，找最小值 + 一行版本

> Author: Benhao
> Date: 2021-11-06
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
我们最关心的是，对于行和对于列最小的变动分别在哪里（两个线性），因为那个变动决定了最大的数的行数和列数（乘起来就是答案要的个数）

### 代码

```Python3 []
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row, col = m, n
        for r, c in ops:
            row = min(row, r)
            col = min(col, c)
        return row * col
```
```Java []
class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int row = m, col = n;
        for(int[] op: ops){
            row = Math.min(row, op[0]);
            col = Math.min(col, op[1]);
        }
        return row * col;
    }
}
```
```JavaScript []
/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function(m, n, ops) {
    let row = m, col = n;
    for(const op of ops){
        row = Math.min(row, op[0]);
        col = Math.min(col, op[1]);
    }
    return row * col;
};
```
```Go []
func maxCount(m int, n int, ops [][]int) int {
    for _, op := range ops {
        if op[0] < m {
            m = op[0]
        }
        if op[1] < n {
            n = op[1]
        }
    }
    return m * n
}
```
应邀写一下一行版本
```Python3
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return m * n if not ops else min((z:=list(zip(*ops)))[0]) * min(z[1])
```