import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSubmat(test_input)

    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        heights = [0] * n
        ans = 0
        for row in mat:
            st = []
            prev = [0] * n
            prev_sum = 0
            for j, val in enumerate(row):
                if val == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1 # 叠加纵向高度
                while st and heights[st[-1]] >= heights[j]: # 单调栈找到当前高度的最大宽度
                    prev_sum -= prev[st.pop()] # 减去之前的贡献
                prev[j] = heights[j] * (j - (st[-1] if st else -1)) # 计算当前高度的贡献
                prev_sum += prev[j] # 累加当前高度的贡献
                st.append(j)
                ans += prev_sum # 累加到答案中
        return ans
