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
        total = [(i,aliceValues[i]+bobValues[i]) for i in range(len(aliceValues))]
        total.sort(key=lambda x:-x[1])
        turn = True
        score = 0
        while total:
            i,_ = total.pop(0)
            if turn:
                score += aliceValues[i]
                turn = False
            else:
                score -= bobValues[i]
                turn = True

        if score > 0:
            return 1
        elif score < 0:
            return -1
        else:
            return 0
