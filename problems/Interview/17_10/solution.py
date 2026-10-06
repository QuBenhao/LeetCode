import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.majorityElement(list(test_input))

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Majority vote algorithm, like voting out a player in Werewolf
        # First pass: find the most likely player to be voted out
        n = len(nums)
        ans = -1
        count = 0
        for num in nums:
            # With no votes left, tentatively choose the current player
            if not count:
                ans = num
            # A vote for the same player increases the count; any other vote decreases it
            if num == ans:
                count += 1
            else:
                count -= 1
        # Second pass: verify that this player has more than half the votes
        return ans if count and nums.count(ans) > n // 2 else -1
