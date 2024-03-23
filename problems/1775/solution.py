import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        elif s1 < s2:
            nums1, nums2 = nums2, nums1
        d = abs(s1-s2)
        div = {5:[6,1],4:[5,2],3:[4,3],2:[3,4],1:[2,5]}
        curr = 5
        left = 0
        op = 0
        while d > 0 and curr > 0:
            c = nums1.count(div[curr][0]) + nums2.count(div[curr][1]) + left
            if d // curr >= c:
                d -= c * curr
                op += c
                left = 0
            else:
                op += d // curr
                d %= curr
                left += c - d // curr
            curr -= 1
        if d > 0:
            return -1
        return op
