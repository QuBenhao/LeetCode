# [Python/Java/JavaScript/Go] 数学

> Author: Benhao
> Date: 2022-05-15
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
方法一: 从网上找一个合适的，从三点坐标计算三角形面积的公式
方法二: 直接cv这里的公式

### 代码

```Python3 []
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2 for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))
```
```Java []
class Solution {
    public double largestTriangleArea(int[][] points) {
        double ans = 0.0;
        for(int i = 0, n = points.length; i < n - 2; i++) {
            for(int j = i + 1; j < n - 1; j++) {
                for(int k = j + 1; k < n; k++) {
                    int x1 = points[i][0], y1 = points[i][1];
                    int x2 = points[j][0], y2 = points[j][1];
                    int x3 = points[k][0], y3 = points[k][1];
                    ans = Math.max(ans, Math.abs((x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2.0));
                }
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function(points) {
    const n = points.length
    let ans = 0.0
    for(let i = 0; i < n - 2; i++) {
        for(let j = i + 1; j < n - 1; j++) {
            for(let k = j + 1; k < n; k++) {
                const [[x1, y1], [x2, y2], [x3, y3]] = [points[i], points[j], points[k]]
                ans = Math.max(ans, Math.abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2)
            }
        }
    }
    return ans
};
```
```Go []
func largestTriangleArea(points [][]int) (ans float64) {
    for i, n := 0, len(points); i < n - 2; i++ {
        for j := i + 1; j < n - 1; j++ {
            for k := j + 1; k < n; k++ {
                x1, y1 := points[i][0], points[i][1]
                x2, y2 := points[j][0], points[j][1]
                x3, y3 := points[k][0], points[k][1]
                d := x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2
                if d < 0 {
                    d *= -1
                }
                if cur := float64(d) / 2.0; cur > ans {
                    ans = cur
                }
            }
        }
    }
    return
}
```