import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfRounds(str(test_input[0]), str(test_input[1]))

    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        # f到s之间有多少个15分钟, 但是01->29这种不能看做15分钟
        start = int(startTime[:2]) * 60 + int(startTime[3:])
        finish = int(finishTime[:2]) * 60 + int(finishTime[3:])
        # 通宵的情况
        if finish < start:
            # 加一天
            finish += 24 * 60
        # 要正点结束
        finish = finish // 15 * 15
        # 这里开始不再需要调整为正点因为地板除15是一致的
        return (finish - start) // 15 if finish > start else 0
