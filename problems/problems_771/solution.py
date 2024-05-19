import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numJewelsInStones(*test_input)

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        # 20ms solution
        # count = 0
        # for c in S:
        #     if c in J:
        #         count += 1
        # return count

        # 16ms solution
        return sum(map(S.count, J))