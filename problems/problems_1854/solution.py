import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumPopulation([x[:] for x in test_input])

    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        people = [0] * 101
        base_year = 1950
        for b,d in logs:
            people[b-base_year] += 1
            people[d-base_year] -= 1
        curr = ans = m = 0
        for i,p in enumerate(people):
            curr += p
            if curr > m:
                m, ans = curr, base_year + i
        return ans
