import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canChoose(*test_input)

    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """

        # # String solution
        s = "#".join(map(str, nums))
        for group in groups:
            g = "#".join(map(str, group))
            i = s.find(g)
            if i == -1:
                return False
            s = s[i + len(g):]
        return True

        # ig, i, ng, n = 0, 0, len(groups), len(nums)
        # while ig < ng:
        #     if i == n:
        #         return False
        #     if nums[i:i+len(groups[ig])] == groups[ig]:
        #         i += len(groups[ig]) - 1
        #         ig += 1
        #     i += 1
        # return True
