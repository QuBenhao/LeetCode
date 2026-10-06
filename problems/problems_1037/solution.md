# [Python/Java/TypeScript/Go] Vector formula for three collinear points

> slug: pythonjavatypescriptgo-by-himymben-i6on
> date: 2022-06-07
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Valid Boomerang (valid-boomerang)
> url: https://leetcode.cn/problems/valid-boomerang/solutions/1gTjsb/pythonjavatypescriptgo-by-himymben-i6on/

---
### Approach
With the college entrance exam approaching, this is a good time to review the vector formula for three collinear points.
The three points are collinear when:
$(x_2 - x_1) \times (y_3 - y_1) = (x_3 - x_1) \times (y_2 - y_1)$
Otherwise, they form a boomerang.

### Code

```Python3 []
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[1][0] - points[0][0]) * (points[2][1] - points[0][1]) != (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
```
```Java []
class Solution {
    public boolean isBoomerang(int[][] points) {
        return (points[1][0] - points[0][0]) * (points[2][1] - points[0][1]) != (points[2][0] - points[0][0]) * (points[1][1] - points[0][1]);
    }
}
```
```TypeScript []
function isBoomerang(points: number[][]): boolean {
    const [[x1, y1], [x2, y2], [x3, y3]] = points
    return (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)
};
```
```Go []
func isBoomerang(points [][]int) bool {
    return (points[1][0] - points[0][0]) * (points[2][1] - points[0][1]) != (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
}
```
