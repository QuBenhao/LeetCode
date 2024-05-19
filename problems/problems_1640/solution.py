import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canFormArray(*test_input)

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
