import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        aliceValues, bobValues = test_input
        return self.stoneGameVI(aliceValues,bobValues)

    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        totalValues = [(a+b) for a,b in zip(aliceValues, bobValues)]
        totalValues.sort(reverse=True)
        # 所有Alice能拿到的石头的总价值，其中每个都多拿了Bob的对应石子,再减去本来就是Bob拿的石子，正好是Bob的所有石子
        ans = sum(totalValues[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
