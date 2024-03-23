import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.memLeak(*test_input)

    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        i = 1
        while True:
            if memory2 > memory1:
                if i > memory2:
                    return [i, memory1, memory2]
                memory2 -= i
            else:
                if i > memory1:
                    return [i, memory1, memory2]
                memory1 -= i
            i += 1
