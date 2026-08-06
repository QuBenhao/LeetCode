# [Python/Java] 容斥原理

> slug: pythonjava-rong-chi-yuan-li-by-himymben-ltmt
> date: 2021-09-29
> tags: Java, Python, Python3
> question: Rectangle Area (rectangle-area)
> url: https://leetcode.cn/problems/rectangle-area/solutions/av4hxL/pythonjava-rong-chi-yuan-li-by-himymben-ltmt/

---
### 解题思路
根据左下、右上角，我们可以很容易求出两个矩阵的面积。但是我们需要知道两个矩阵是否有交集(矩阵)，而这个矩阵的左下角应该由两个矩阵的左下角延x，y轴方向的射线的交点构成；这个矩阵的右上角由两个矩阵的右上角延x，y轴方向的射线的交点构成。如果这个交集矩阵的右上角在左下角左下方，说明构不成一个交集矩阵。

详细看【宫水三叶】的[题解](https://leetcode.cn/problems/rectangle-area/solution/gong-shui-san-xie-yun-yong-rong-chi-yuan-hzit/)。

### 代码

```python3 []
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 交集矩阵的右上角的横坐标为 ax2,bx2中更小的那个；左下角的横坐标为ax1,bx1中更大的那个；
        # 但是这并不能保证交集矩阵的右上角一定比左上角大，我们不允许负数的边长，所以取max(0, 边长)
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1))    
```
```Java []
class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int interaction_x = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1));
        int interaction_y = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - interaction_x * interaction_y;
    }
}
```