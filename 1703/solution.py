import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.minMoves(nums.copy(), k)

    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        if k % 2 == 1:
            radius = (k - 1) // 2
            save = radius * (radius + 1)
        else:
            radius = k // 2 - 1
            save = (radius + 1) ** 2

        n = len(nums)
        prefix = [i for i in range(n) if nums[i]]
        window = []

        ans = float("inf")
        left = right = 0

        while prefix:
            while len(window) < k:
                window.append(prefix.pop(0))
                if len(window) <= radius:
                    left += window[-1]
                elif len(window) > radius + 1:
                    right += window[-1]
            if k % 2 == 1:
                ans = min(ans, right - left)
            else:
                ans = min(ans, right - left - window[radius])
            left += window[radius]
            right -= window[radius+1]
            left -= window.pop(0)

        return ans - save
