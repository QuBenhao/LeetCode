import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.peakIndexInMountainArray(list(test_input))

    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 1, len(arr) - 2
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
