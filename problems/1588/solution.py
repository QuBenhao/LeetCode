import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOddLengthSubarrays(test_input)

    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 长度为n的数组，第一位出现在多少个奇数长度的子数组？
        # 1, 3, 5, ..., length-1/length
        # (length + 1)//2
        n = len(arr)
        l, r, ans, times = 0, n - 1, 0, (n + 1) // 2
        while l <= r:
            # 对称性，前后对称位置出现的次数一样
            if l < r:
                ans += times * (arr[l] + arr[r])
            else:
                ans += times * arr[l]
            l += 1
            r -= 1
            # 下一个数比前一个数多了后一个数构成的不带前一个数的奇数子数组的个数
            times += (n - l + 1) // 2
            # 下一个数比前一个数少了前一个数构成的不带后一个数的奇数子数组的个数
            times -= (l + 1) // 2
        return ans
