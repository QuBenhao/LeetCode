import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.letterCombinations(str(test_input))

    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res = self.letterCombinations(digits[1:])
        if not res:
            return list(self.phone[digits[0]])
        ans = []
        for c in self.phone[digits[0]]:
            for s in res:
                ans.append(c + s)
        return ans
