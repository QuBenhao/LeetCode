import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validPalindrome(test_input)

    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(st: str):
            return st == st[::-1]
            
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        return True
