import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        arr, pieces = test_input
        return self.canFormArray(list(arr), [x[:] for x in pieces])

    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        for p in pieces:
            try:
                i = arr.index(p[0])
                if arr[i:i+len(p)] != p:
                    return False
            except:
                return False
        return True
