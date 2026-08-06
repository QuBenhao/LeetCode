# [Python] 转置矩阵

> slug: python-zhuan-zhi-ju-zhen-by-himymben-ioy2
> date: 2022-03-13
> tags: Python, Python3
> question: Transpose Matrix (transpose-matrix)
> url: https://leetcode.cn/problems/transpose-matrix/solutions/6lT3IC/python-zhuan-zhi-ju-zhen-by-himymben-ioy2/

---
```python3
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
```