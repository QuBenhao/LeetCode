import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.averageWaitingTime([x[:] for x in test_input])

    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        curr_time = 0
        wait = 0.0
        for a,t in customers:
            if a >= curr_time:
                wait += t
                curr_time = a + t
            else:
                wait += curr_time - a + t
                curr_time += t
        return wait/len(customers)
