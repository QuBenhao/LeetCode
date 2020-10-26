import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkPossibility(test_input)

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        mark = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                mark = i
        if count > 1:
            return False
        elif count == 1:
            if 0 < mark < len(nums)-2:
                if nums[mark-1] > nums[mark+1] and nums[mark] > nums[mark+2]:
                    return False
        return True
