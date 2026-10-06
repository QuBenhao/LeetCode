import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfRounds(*test_input)

    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        # Count complete quarter-hours between s and f; 01->29 does not contain one
        start = int(startTime[:2]) * 60 + int(startTime[3:])
        finish = int(finishTime[:2]) * 60 + int(finishTime[3:])
        # Overnight case
        if finish < start:
            # Add one day
            finish += 24 * 60
        # The finish must fall on a quarter-hour boundary
        finish = finish // 15 * 15
        # No need to adjust the start to a boundary here, since floor division by 15 gives the same result
        return (finish - start) // 15 if finish > start else 0
