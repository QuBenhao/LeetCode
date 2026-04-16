# [Python] 两种方法：依次螺旋填数，到达边界右转（顺时针）

> Author: Benhao
> Date: 2021-03-15
> Upvotes: 1
> Tags: Python

---

### 解题思路
从左上角出发开始转圈，通过前面有没有被填过来判断是不是需要转向。

另一种思路就是每圈看成四个边组成，手动卡边界，特殊情况只有n=1时，没有四个边只有一个。

### 代码

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            ans[i][j] = k + 1
            if ans[(i + di)%n][(j+dj)%n]:
                # 0, 1 -> 1, 0 -> 0, -1 -> -1, 0
                di, dj = dj, -di
            i += di
            j += dj
        return ans
```

```python
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        i, j, curr = 0, 0, 1
        while n > 1:
            for j in range(j, j + n-1):
                ans[i][j] = curr
                curr += 1
            j += 1
            for i in range(i, i +n-1):
                ans[i][j] = curr
                curr += 1
            i += 1
            for j in range(j, j-n+1, -1):
                ans[i][j] = curr
                curr += 1
            j -= 1
            for i in range(i, i-n+1, -1):
                ans[i][j] = curr
                curr += 1
            j += 1
            n -= 2
        if n == 1:
            ans[i][j] = curr
        return ans
```

```python
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        x, y, curr = 0, 0, 1
        while n > 1:
            for j in range(4):
                for i in range(n-1):
                    ans[x][y] = curr
                    if j == 0:
                        y += 1
                    elif j == 1:
                        x += 1
                    elif j == 2:
                        y -= 1
                    else:
                        x -= 1
                    curr += 1
            x += 1
            y += 1
            n -= 2
        if n == 1:
            ans[x][y] = curr
        return ans
```