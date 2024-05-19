import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBeautifulSubstring(str(test_input))

    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = count = 0
        check = {'a', 'e', 'i', 'o', 'u'}
        explored = set()
        word += 'a'
        for i,c in enumerate(word):
            if i and word[i-1] > c:
                if explored == check:
                    ans = max(ans, count)
                count = 1
                explored = set()
            else:
                count += 1
            explored.add(c)
        return ans
