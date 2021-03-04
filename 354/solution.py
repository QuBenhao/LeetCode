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
            # dp[i]: 长度为i+1的子数列中最小的尾数
            dp = [0] * n
            for i in range(n):
                # 保持dp的更新可以保证每次二分查找时，找到的都是nums[i]可以和之前组成的最长递增子数列的长度
                # 也就是left最后的值是包含nums[i]的最长递增子数列的长度-1
                left, right = 0, length
                while left < right:
                    mid = (left + right) // 2
                    if dp[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid + 1
                if left == length:
                    length += 1
                # if left == length, 显然nums[i] > dp[length-1], dp变为长度加一的最长递增子数列
                # if left < length, 显然存在 0 < j < length 使得 dp[j-1] < nums[i] <= dp[j] 或者 nums[i] <= dp[0]，
                # 第一种情况下，长度为j+1的最长递增子数列的最小尾数就要更新为nums[i];
                # 第二种情况下，dp[0] = nums[i]， 实际上也代表了nums[i] = min(nums[:i+1])
                dp[left] = nums[i]
            return length

        # 按w递增排序、h递减排序可以保证在找h的最长递增子数列的时候，w也是递增的 (h的逆序排列保证相同的w不可能在h里出现两次)
        return lengthOfLIS([x[1] for x in sorted(envelopes, key=lambda x:(x[0],-x[1]))])
