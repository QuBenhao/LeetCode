import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOddLengthSubarrays(test_input)

    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # How many odd-length subarrays of an array of length n contain the first position?
        # 1, 3, 5, ..., length-1/length
        # (length + 1)//2
        n = len(arr)
        l, r, ans, times = 0, n - 1, 0, (n + 1) // 2
        while l <= r:
            # By symmetry, mirrored positions have equal counts
            if l < r:
                ans += times * (arr[l] + arr[r])
            else:
                ans += times * arr[l]
            l += 1
            r -= 1
            # Add odd-length subarrays containing the next number but not the previous one
            times += (n - l + 1) // 2
            # Subtract odd-length subarrays containing the previous number but not the next one
            times -= (l + 1) // 2
        return ans
