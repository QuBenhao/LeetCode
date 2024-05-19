import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalMoney(test_input)

    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        days = total = start = last = 0
        while days < n:
            if days % 7 == 0:
                start += 1
                total += start
                last = start
            else:
                last += 1
                total += last
            days += 1
        return total
