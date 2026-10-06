# [Python] Compare clockwise rotations by 0, 90, 180, and 270 degrees

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
Too lazy to explain; see the code.

### Code

```python3
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            m,n = len(matrix),len(matrix[0])
            new = [[0] * m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    new[j][m-1-i] = matrix[i][j]
            return new
        
        if mat == target:
            return True
        
        for i in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        return False
```
