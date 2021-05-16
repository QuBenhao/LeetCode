import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOddLengthSubarrays(test_input)

    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        """
        The frequency of current num is based on the frequency of last num 
        except the subarray that contains the last element but not current element
        and add the subarray that contains the current element but not the last element.
        
        The frequency of the first element is how many odds number from 1 to the length of array.
        """
        res = 0
        freq = 0
        n = len(arr)
        for i in range(n):
            freq = freq - (i + 1) // 2 + (n - i + 1) // 2
            res += freq * arr[i]
        return res
