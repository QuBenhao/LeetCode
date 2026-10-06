# [Python/Java] Inclusion-exclusion principle

> slug: pythonjava-rong-chi-yuan-li-by-himymben-ltmt
> date: 2021-09-29
> tags: Java, Python, Python3
> question: Rectangle Area (rectangle-area)
> url: https://leetcode.cn/problems/rectangle-area/solutions/av4hxL/pythonjava-rong-chi-yuan-li-by-himymben-ltmt/

---
### Approach
The areas of the two rectangles are easy to compute from their bottom-left and top-right corners. We also need to determine whether they intersect in a rectangle. Its bottom-left corner comes from intersecting rays along the x and y axes from the original bottom-left corners; its top-right corner similarly comes from the original top-right corners. If the resulting top-right corner lies below and to the left of the bottom-left corner, no intersection rectangle can be formed.

For details, see the [solution](https://leetcode.cn/problems/rectangle-area/solution/gong-shui-san-xie-yun-yong-rong-chi-yuan-hzit/) by 【宫水三叶】.

### Code

```python3 []
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # The intersection's top-right x coordinate is the smaller of ax2,bx2; its bottom-left x coordinate is the larger of ax1,bx1
        # This does not guarantee a positive side length for the intersection, so use max(0, side length) to disallow negative lengths
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
