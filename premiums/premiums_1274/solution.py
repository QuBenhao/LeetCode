import solution
from typing import *


# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countShips(*test_input)

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
                pass
        