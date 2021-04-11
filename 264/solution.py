import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nthUglyNumber(test_input)

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        p2 = p3 = p5 = 0
        while len(nums) < n:
            nums.append(min(nums[p2] * 2, nums[p3]*3, nums[p5] * 5))
            if nums[-1] == nums[p2] * 2:
                p2 += 1
            if nums[-1] == nums[p3] * 3:
                p3 += 1
            if nums[-1] == nums[p5] * 5:
                p5 += 1
        return nums[-1]
