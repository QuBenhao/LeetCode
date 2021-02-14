import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countHomogenous(str(test_input))

    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter()
        n, last, index = len(s), s[0], 0
        if n == 1:
            return 1
        s += "#"
        n += 1
        for i in range(1, n):
            if s[i] != s[i-1]:
                count[s[index:i]] += 1
                index = i
        ans = 0
        for key in count:
            ans += (len(key)+1)*len(key)*count[key]//2
        return ans % (10**9 + 7)
