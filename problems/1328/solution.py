import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.breakPalindrome(str(test_input))

    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(palindrome)
        if n == 1:
            return ""

        mid = n//2
        for i in range(mid):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:n-1] + 'b'
