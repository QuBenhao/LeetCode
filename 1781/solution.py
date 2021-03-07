import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.beautySum(str(test_input))

    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        li = []
        for c in s:
            new = [0] * 26
            i = ord(c) - ord('a')
            new[i] = 1
            for counter in li:
                counter[i] += 1
                ans += max(counter) - min(k for k in counter if k)
            li.append(new)
        return ans
