import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaxLength(list(test_input))

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Prefix sum dictionary: key is the difference between counts of ones and zeros; value is its index
        hashmap = {0:-1}
        # Current difference between counts of ones and zeros
        counter = ans = 0
        for i,num in enumerate(nums):
            # Each additional one increases the difference by 1
            if num:
                counter += 1
            # Each additional zero decreases the difference by 1
            else:
                counter -= 1
            # Equal prefix differences mean the interval between them contains equal numbers of ones and zeros!
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans
