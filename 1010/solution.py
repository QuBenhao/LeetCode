import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numPairsDivisibleBy60(test_input)

    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        counter = [0] * 60
        for t in time:
            counter[t % 60] += 1
        count = 0
        count += counter[0] * (counter[0] - 1) / 2
        count += counter[30] * (counter[30] - 1) / 2
        for i in range(1, 30):
            if counter[i] == 0:
                continue
            count += counter[i] * counter[60 - i]
        return int(count)
