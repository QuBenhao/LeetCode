import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largeGroupPositions(str(test_input))

    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        i = start = 0
        curr = s[start]
        ans = []
        while True:
            if i == len(s):
                if i - start > 2:
                    ans.append([start, i - 1])
                break
            if s[i] != curr:
                if i - start > 2:
                    ans.append([start, i - 1])
                start = i
                curr = s[start]
            i += 1
        return ans
