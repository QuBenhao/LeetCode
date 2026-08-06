# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-73si
> date: 2022-02-14
> tags: Go, Java, JavaScript, Python, Python3
> question: Lucky Numbers in a Matrix (lucky-numbers-in-a-matrix)
> url: https://leetcode.cn/problems/lucky-numbers-in-a-matrix/solutions/OcAim5/pythonjavajavascriptgo-mo-ni-by-himymben-73si/

---
### 解题思路
这样的点至多有一个，我们只需要确定某行最小值的最大值与某列最大值的最小值一致

1. 证明
反证法：
假设有两个点`x1,y1`和`x2,y2`，它们都是幸运数。
根据题目描述，我们有以下大小关系：
> matrix[x1][y1] <= matrix[x1][y2] (行最小)
> matrix[x1][y1] >= matrix[x2][y1] (列最大)
> matrix[x2][y2] <= matrix[x2][y1] (行最小)
> matrix[x2][y2] >= matrix[x1][y2] (列最大)

我们会发现:
> matrix[x2][y2] >= matrix[x1][y2] >= matrix[x1][y1]
> matrix[x1][y1] >= matrix[x2][y1] >= matrix[x2][y2]

所以只有`matrix[x1][y1] == matrix[x2][y2]`这一种情况，
但是题目给出了数字各不相同，矛盾。


2. 为什么是行的最小值的最大值和列的最大值的最小值

假设我们没有取行的最小值的最大值，设取得行`r1`，那么一定存在某一行`r2`的最小值大于`r1`。
那么`r1`的最小值那一列是一定小于`r2`的该列的值的（因为最小值比`r2`的最小值还小）
显然这样的`r1`最小值必然不满足该列最大值。
故我们必须取行的最小值的最大值。
同理可以证明我们必须取列的最大值的最小值。
又因为答案最多一个，故只有这两个值相等，才存在答案

### 代码

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

### 复杂度
时间复杂度$O(m * n)$
空间复杂度$O(1)$