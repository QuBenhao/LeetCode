import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameVI(*test_input)

    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        totalValues = [(a+b) for a,b in zip(aliceValues, bobValues)]
        totalValues.sort(reverse=True)
        # Sum the combined values of Alice's stones, then subtract all of Bob's valuations to obtain the score difference
        ans = sum(totalValues[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
