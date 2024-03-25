import solution
from typing import *


# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        :type fontSize: int
#        :type ch: char
#        :rtype int
# 
#    def getHeight(self, fontSize):
#        :type fontSize: int
#        :rtype int
class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFont(*test_input)

    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
                    pass
        