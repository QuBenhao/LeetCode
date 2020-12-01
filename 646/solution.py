import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLongestChain(test_input)

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[1])
        length = 0
        curr = pairs[0][0] - 1
        for i in range(len(pairs)):
            if pairs[i][0] <= curr:
                continue
            length += 1
            curr = pairs[i][1]
        return length
