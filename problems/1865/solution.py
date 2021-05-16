import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        op1,vals = test_input
        ans = [None]
        obj = FindSumPairs(vals[0][0], vals[0][1])
        for i in range(1, len(op1)):
            if op1[i] == "count":
                ans.append(obj.count(vals[i][0]))
            else:
                obj.add(vals[i][0],vals[i][1])
                ans.append(None)
        return ans


class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.c1 = Counter(nums1)
        self.nums2 = nums2
        self.c2 = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.c2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.c2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        return sum(self.c1[i] * self.c2[tot-i] for i in self.c1)
