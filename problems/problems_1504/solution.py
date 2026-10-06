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
                    heights[j] += 1 # Accumulate column heights
                while st and heights[st[-1]] >= heights[j]: # Use a monotonic stack to find the maximum width for the current height
                    prev_sum -= prev[st.pop()] # Subtract the previous contribution
                prev[j] = heights[j] * (j - (st[-1] if st else -1)) # Compute the contribution of the current height
                prev_sum += prev[j] # Accumulate the contribution of the current height
                st.append(j)
                ans += prev_sum # Add it to the answer
        return ans
