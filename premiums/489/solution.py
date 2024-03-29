import solution
from typing import *


# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
#class Robot:
#    def move(self):
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#
#    def turnLeft(self):
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#
#    def turnRight(self):
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#
#    def clean(self):
#        Clean the current cell.
#        :rtype void

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.cleanRoom(*test_input)

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        pass
        