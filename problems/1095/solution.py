import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        arr, target = test_input
        mountain_arr = MountainArray(arr)
        return self.findInMountainArray(target, mountain_arr)

    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = int((l + r) / 2)
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = int((l + r) / 2)
            num = mountain_arr.get(m)
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = int((l + r) / 2)
            num = mountain_arr.get(m)
            if num > target:
                l = m + 1
            elif num < target:
                r = m - 1
            else:
                return m
        return -1


class MountainArray(object):
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        """
        :type index: int
        :rtype int
        """
        return self.arr[index]

    def length(self):
        """
        :rtype int
        """
        return len(self.arr)
