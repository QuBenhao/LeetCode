import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validMountainArray(test_input)

    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        increase = True
        for i in range(1, len(arr) - 1):
            if increase and arr[i] >= arr[i + 1]:
                increase = False
            if not increase and arr[i] <= arr[i + 1]:
                return False
        return not increase
