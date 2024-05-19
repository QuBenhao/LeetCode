import solution
from functools import cmp_to_key


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestNumber(list(test_input))

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # compare two string by x+y and y+x, place the greater one in front of the other
        return str(int("".join(sorted(map(str, nums),key=cmp_to_key(lambda x,y:((x+y) < (y+x)) - ((x+y) > (y+x)))))))
