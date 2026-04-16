# [Python] 贪心(天花板)

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
想象三栋楼的最高高度为target。
如果有个triplet任意一个值超过最高高度，这个triplet必然不能参与任何运算中(超过天花板不能再回来了)。
那么剩下的能用的triplets中每个triplet的值都是小于等于每个天花板的，这个时候我们只要关心能不能取到天花板的值就行了。(全部操作后最终每个位置都会变成每个位置的最大值)

### 代码

```python3
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        x_ = y_ = z_ = False
        for a,b,c in list(triplets):
            if a > x or b > y or c > z:
                continue
            if a == x:
                x_ = True
            if b == y:
                y_ = True
            if c == z:
                z_ = True
        return x_ and y_ and z_
```