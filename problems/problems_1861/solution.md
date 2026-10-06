# [Python] Rotate while counting stones stopped by obstacles

> Author: Benhao
> Date: 2021-05-15
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Each obstacle stops only the stones to its left. Reset the count afterward; subsequent stones belong to the next obstacle.
Finally, handle stones that fall against the implicit bottom boundary.

### Code

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
