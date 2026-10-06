import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxEnvelopes([x[:] for x in test_input])

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def lengthOfLIS(nums):
            length, n = 0, len(nums)
            # dp[i]: the smallest tail value of a subsequence of length i+1
            dp = [0] * n
            for i in range(n):
                # Updating dp ensures that binary search finds the longest increasing subsequence that nums[i] can extend
                # Thus, the final left is the length of the longest increasing subsequence ending at nums[i] minus 1
                left, right = 0, length
                while left < right:
                    mid = (left + right) // 2
                    if dp[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid + 1
                if left == length:
                    length += 1
                # If left == length, then nums[i] > dp[length-1], extending the longest increasing subsequence by one
                # If left < length, either some 0 < j < length satisfies dp[j-1] < nums[i] <= dp[j], or nums[i] <= dp[0]
                # In the first case, update the minimum tail for a subsequence of length j+1 to nums[i]
                # In the second case, dp[0] = nums[i], also meaning nums[i] = min(nums[:i+1])
                dp[left] = nums[i]
            return length

        # Sort w ascending and h descending so that an LIS in h also has increasing w (descending h prevents using the same w twice)
        return lengthOfLIS([x[1] for x in sorted(envelopes, key=lambda x:(x[0],-x[1]))])
