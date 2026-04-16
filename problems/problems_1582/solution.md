# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-09-04
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
求和为1的行、和为1的列，
再统计他们的交点是不是1的个数。

### 代码

```Python3 []
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(mat[r][c] for r, c in product(rows, cols)) if (rows := [i for i in range(len(mat)) if sum(mat[i]) == 1 ]) and (cols := [i for i, col in enumerate(zip(*mat)) if sum(col) == 1]) else 0
```
```Java []
class Solution {
    public int numSpecial(int[][] mat) {
        List<Integer> rows = new ArrayList<>(), cols = new ArrayList<>();
        for (int i = 0; i < mat.length; i++) {
            int s = 0;
            for (int j = 0; j < mat[0].length; j++) {
                s += mat[i][j];
            }
            if (s == 1) {
                rows.add(i);
            }
        }
        for (int i = 0; i < mat[0].length; i++) {
            int s = 0;
            for (int j = 0; j < mat.length; j++) {
                s += mat[j][i];
            }
            if (s == 1) {
                cols.add(i);
            }
        }
        int ans = 0;
        for (int i: rows) {
            for (int j: cols) {
                ans += mat[i][j];
            }
        }
        return ans;
    }
}
```
```TypeScript []
function numSpecial(mat: number[][]): number {
    const rows: Array<number> = new Array<number>(), cols: Array<number> = new Array<number>()
    for (let i = 0; i < mat.length; i++) {
        if (mat[i].reduce((a, b) => a + b) == 1) {
            rows.push(i)
        }
    }
    for (let i = 0; i < mat[0].length; i++) {
        let s: number = 0
        for (let j = 0; j < mat.length; j++) {
            s += mat[j][i]
        }
        if (s == 1) {
            cols.push(i)
        }
    }
    let ans: number = 0
    rows.forEach(i => cols.forEach(j => ans += mat[i][j]))
    return ans
};
```
```Go []
func numSpecial(mat [][]int) (ans int) {
    rows, cols := []int{}, []int{}
    for i, row := range mat {
        if sum(row) == 1 {
            rows = append(rows, i)
        }
    }
    for i := 0; i < len(mat[0]); i++ {
        s := 0
        for j := 0; j < len(mat); j++ {
            s += mat[j][i]
        }
        if s == 1 {
            cols = append(cols, i)
        }
    }
    for _, i := range rows {
        for _, j := range cols {
            ans += mat[i][j]
        }
    }
    return
}

func sum(nums []int) (ans int) {
    for _, v := range nums {
        ans += v
    }
    return
}
```