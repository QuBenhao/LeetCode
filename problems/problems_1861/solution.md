# [Python] 一边旋转一边统计被障碍物卡住的石子

> Author: Benhao
> Date: 2021-05-15
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
每个障碍物只能卡住它左边的石子，然后清空计数，剩下的计的就是给下一个障碍物了。
最后看看默认的底部障碍物有没有石子

### 代码

```python3
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [['.'] * m for _ in range(n)]
        for i in range(m):
            count = 0
            for j in range(n):
                if box[i][j] == '*':
                    ans[j][m-1-i] = '*'
                    for k in range(1, count+1):
                        ans[j-k][m-1-i] = '#'
                    count = 0
                elif box[i][j] == '#':
                    count += 1
            if count:
                for k in range(count):
                    ans[n-1-k][m-1-i] = '#'
        return ans
```