import solution
from typing import *


# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getIndex(*test_input)

    def getIndex(self, reader: 'ArrayReader') -> int:
            pass
        