import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfUnique(list(test_input))

    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        explored = set()
        minus = set()
        ans = 0
        for num in nums:
            if num in explored:
                if num not in minus:
                    minus.add(num)
                    ans -= num
            else:
                explored.add(num)
                ans += num
        return ans
