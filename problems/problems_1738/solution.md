# [Python] 二维前缀异或

> Author: Benhao
> Date: 2021-05-19
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
因为异或中,有`x^x = 0` 
根据容斥原理，`matrix[i][j] = matrix[i][j] ^ matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]`

### 代码

```python3

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
                elif i:
                    matrix[i][j] ^= matrix[i-1][j]
                elif j:
                    matrix[i][j] ^= matrix[i][j-1]
        return sorted([j for i in matrix for j in i])[-k]

```