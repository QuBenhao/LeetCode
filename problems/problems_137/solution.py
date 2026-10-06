import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNumber(test_input.copy())

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Count bits
        # cnt = [0] * 32
        # for num in nums:
        #     for i in range(32):
        #         # Check whether the ith bit from the right is 1
        #         if (num >> i) & 1:
        #             cnt[i] += 1
        # ans = 0
        # for i in range(32):
        #     if cnt[i] % 3:
        #         # In Python, a 1 in the 32nd bit indicates a negative number
        #         if i == 31:
        #             ans -= (1 << i)
        #         else:
        #             ans += (1 << i)
        # return ans

        """
        Truth table conversion approach
        00 - one occurrence -> 01 - one occurrence -> 10 - one occurrence -> 00
        Using two bits a and b to represent three states, we have:
        a,b,x -> a b
        0 0 0 -> 0 0
        0 0 1 -> 0 1
        0 1 0 -> 0 1
        0 1 1 -> 1 0
        1 0 0 -> 1 0
        1 0 1 -> 0 0
        That is:
        When updating a and b simultaneously:
        a, b = (a & ~x) | (b & x), b ^ x & ~a
        
        When updating b first, then using the new b to update a:
        b = b ^ x & ~a
        a = a ^ x & ~b
        """
        a = b = 0
        for num in nums:
            # a, b = (a & ~num) | (b & num), b ^ num & ~a
            b = b ^ num & ~a
            a = a ^ num & ~b
        return b
