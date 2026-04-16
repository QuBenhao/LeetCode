# [Python] 差分数组

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
差分是对这个区间内全部加上这个颜色的一个好办法，然后判断颜色相同的一个区间；
另外，
可能写的比较麻烦，要额外判断颜色相等时，他们是不是由不同的端点组成了。

### 代码

```python3
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = [0] * 100005
        points = set()
        right = 0
        for a, b, c in segments:
            diff[a] += c
            diff[b] -= c
            right = max(right, b)
            points.add(a)
            points.add(b)
        ans = []
        curr = 0
        left = None
        color = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if color and curr != color:
                if color and left is not None:
                    ans.append([left, i, color])
                if curr:
                    left = i
                    color = curr
                else:
                    left = None
            elif color and curr == color:
                if i in points and left is not None:
                    ans.append([left, i, color])
                    left = i
            if curr and left is None:
                left = i
                color = curr
        return ans
```