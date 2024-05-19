import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestObstacleCourseAtEachPosition(list(test_input))

    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = []
        for num in obstacles:
            if not stack or stack[-1] <= num:
                stack.append(num)
                ans.append(len(stack))
            else:
                idx = bisect.bisect_right(stack, num)
                stack[idx] = num
                ans.append(idx + 1)
        return ans
