import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        arr, k = test_input
        return self.findKthPositive(list(arr), k)

    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        def helper(arr, k, last_value):
            if not arr or k < arr[0] - last_value:
                return last_value + k
            k -= arr[0] - last_value - 1
            last_value = arr.pop(0)
            return helper(arr, k, last_value)

        return helper(arr, k, 0)
