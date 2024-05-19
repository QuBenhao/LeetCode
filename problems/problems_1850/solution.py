import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getMinSwaps(*test_input)

    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        n = len(num)
        num = list(num)
        nums = list(num)
        while k:
            i = n - 2
            while i >= 0:
                if nums[i] < nums[i + 1]:
                    break
                i -= 1
            j = n - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums = nums[:i + 1] + sorted(nums[i + 1:])
            k -= 1

        ans = 0
        for i in range(n):
            j = i
            while j < n and nums[i] != num[j]:
                j += 1
            ans += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return ans
