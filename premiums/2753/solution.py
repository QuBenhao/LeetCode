import solution
from typing import *


class Street:
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass

# Definition for a street.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        street, k = test_input
        return self.houseCount(street, k)

    def houseCount(self, street: Optional['Street'], k: int) -> int:
            pass
        