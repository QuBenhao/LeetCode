import solution
from typing import *


# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findShortestPath(*test_input)

    def findShortestPath(self, master: 'GridMaster') -> int:
            pass
        