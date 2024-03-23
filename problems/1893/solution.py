import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isCovered(*test_input)

    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
        
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        curr = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if curr <= 0 and left <= i:
                return False
        return True
