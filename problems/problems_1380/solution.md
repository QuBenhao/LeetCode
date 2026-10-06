# [Python/Java/JavaScript/Go] Simulation

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-73si
> date: 2022-02-14
> tags: Go, Java, JavaScript, Python, Python3
> question: Lucky Numbers in a Matrix (lucky-numbers-in-a-matrix)
> url: https://leetcode.cn/problems/lucky-numbers-in-a-matrix/solutions/OcAim5/pythonjavajavascriptgo-mo-ni-by-himymben-73si/

---
### Approach
There is at most one such cell. Check whether the largest row minimum equals the smallest column maximum.

1. Proof
Proof by contradiction:
Suppose two cells, `x1,y1` and `x2,y2`, are both lucky numbers.
The problem's conditions give these inequalities:
> matrix[x1][y1] <= matrix[x1][y2] (row minimum)
> matrix[x1][y1] >= matrix[x2][y1] (column maximum)
> matrix[x2][y2] <= matrix[x2][y1] (row minimum)
> matrix[x2][y2] >= matrix[x1][y2] (column maximum)

It follows that:
> matrix[x2][y2] >= matrix[x1][y2] >= matrix[x1][y1]
> matrix[x1][y1] >= matrix[x2][y1] >= matrix[x2][y2]

The only possibility is therefore `matrix[x1][y1] == matrix[x2][y2]`.
But the problem states that all values are distinct, a contradiction.


2. Why use the largest row minimum and the smallest column maximum?

Suppose the chosen row `r1` does not have the largest row minimum. Then some row `r2` has a minimum greater than that of `r1`.
The minimum in `r1` must be smaller than the value in the same column of `r2`, since it is even smaller than the minimum of `r2`.
Thus, the minimum in `r1` cannot be the maximum of that column.
We must therefore choose the largest row minimum.
The same reasoning shows that we must choose the smallest column maximum.
Since there is at most one answer, it exists only when these two values are equal.

### Code

```Python3 []
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [a] if (a := max(min(m) for m in matrix)) == (b := min(max(m) for m in zip(*matrix))) else []
```
```Java []
class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int a = 0, b = 100005;
        for(int i = 0; i < matrix.length; i++) {
            int cur = 100005;
            for(int j = 0; j < matrix[i].length; j++)
                cur = Math.min(cur, matrix[i][j]);
            a = Math.max(a, cur);
        }
        for(int j = 0; j < matrix[0].length; j++) {
            int cur = 0;
            for(int i = 0; i < matrix.length; i++) {
                cur = Math.max(cur, matrix[i][j]);
            }
            b = Math.min(b, cur);
        }
        List<Integer> res = new ArrayList<>();
        if(a == b)
            res.add(a);
        return res;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers  = function(matrix) {
    let a = 0, b = 100005
    for(let i = 0; i < matrix.length; i++) {
        let cur = 100005
        for(let j = 0; j < matrix[i].length; j++)
            cur = Math.min(cur, matrix[i][j])
        a = Math.max(a, cur)
    }
    for(let j = 0; j < matrix[0].length; j++) {
        let cur = 0
        for(let i = 0; i < matrix.length; i++)
            cur = Math.max(cur, matrix[i][j])
        b = Math.min(b, cur)
    }
    return a == b ? [a] : []
};
```
```Go []
func luckyNumbers (matrix [][]int) []int {
    a, b := 0, 100005
    for _, row := range matrix {
        cur := 100005
        for _, v := range row {
            cur = min(v, cur)
        }
        a = max(a, cur)
    }
    for j := 0; j < len(matrix[0]); j++ {
        cur := 0
        for i := 0; i < len(matrix); i++ {
            cur = max(matrix[i][j], cur)
        }
        b = min(b, cur)
    }
    if a == b {
        return []int{a}
    }
    return []int{}
}

func min (a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max (a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

### Complexity
Time complexity: $O(m * n)$
Space complexity: $O(1)$
