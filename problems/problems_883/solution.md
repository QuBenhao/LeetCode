# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-tls4
> date: 2022-04-25
> tags: Go, Java, JavaScript, Python, Python3
> question: Projection Area of 3D Shapes (projection-area-of-3d-shapes)
> url: https://leetcode.cn/problems/projection-area-of-3d-shapes/solutions/iwzY8o/pythonjavajavascriptgo-by-himymben-tls4/

---
### 解题思路
xy平面的投影面积为: 数组中非0的总个数。
xz平面的投影面积为: 每行最大值。
yz平面的投影面积为: 每列最大值。

### 代码

```Python3 []
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(sum(v > 0 for v in g) + max(g) for g in grid) + sum(max(g) for g in zip(*grid))
```
```Java []
class Solution {
    public int projectionArea(int[][] grid) {
        int xy = 0, xz = 0, yz = 0;
        for(int[] g: grid) {
            int m = 0;
            for(int v: g) {
                m = Math.max(m, v);
                if(v > 0)
                    xy++;
            }
            xz += m;
        }
        for(int col = 0; col < grid[0].length; col++) {
            int m = 0;
            for(int row = 0; row < grid.length; row++)
                m = Math.max(m, grid[row][col]);
            yz += m;
        }
        return xy + xz + yz;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} grid
 * @return {number}
 */
var projectionArea = function(grid) {
    let xy = 0, xz = 0, yz = 0
    for(const g of grid) {
        let m = 0
        for(const v of g) {
            m = Math.max(m, v)
            if(v > 0)
                xy++
        }
        xz += m
    }
    for(let c = 0; c < grid[0].length; c++) {
        let m = 0
        for(let r = 0; r < grid.length; r++)
            m = Math.max(m, grid[r][c])
        yz += m
    }
    return xy + xz + yz
};
```
```Go []
func projectionArea(grid [][]int) (ans int) {
    for _, g := range grid {
        m := 0
        for _, v := range g {
            if v > 0 {
                if v > m {
                    m = v
                }
                ans++
            }
        }
        ans += m
    }
    for c := 0; c < len(grid[0]); c++ {
        m := 0
        for r := 0; r < len(grid); r++ {
            if grid[r][c] > m {
                m = grid[r][c]
            }
        }
        ans += m
    }
    return
}
```