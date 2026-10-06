# [Python/Java/JavaScript/Go] Treat each dimension independently and find its minimum + one-line version

> Author: Benhao
> Date: 2021-11-06
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
What matters is the smallest update boundary for rows and for columns, considered independently. These determine how many rows and columns contain the maximum value; their product is the answer.

### Code

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
A one-line version, as requested
```Python3
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return m * n if not ops else min((z:=list(zip(*ops)))[0]) * min(z[1])
```
