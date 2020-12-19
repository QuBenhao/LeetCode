import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestWPI(test_input)

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        """
        We starts with a score = 0,
        If the working hour > 8, we plus 1 point.
        Otherwise we minus 1 point.
        We want find the maximum interval that have strict positive score.
        
        After one day of work, if we find the total score > 0,
        the whole interval has positive score,
        so we set res = i + 1.
        
        If the score is a new lowest score, we record the day by seen[cur] = i.
        seen[score] means the first time we see the score is seen[score]th day.
        
        We want a positive score, so we want to know the first occurrence of score - 1.
        score - x also works, but it comes later than score - 1.
        So the maximum interval is i - seen[score - 1]
        """
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res

        # current_value = 0
        # ans = 0
        # d = {}
        #
        # for i in range(len(hours)):
        #     current_value += 1 if hours[i] > 8 else -1
        #
        #     if current_value > 0:
        #         ans = i + 1
        #     else:
        #         if current_value not in d:
        #             d[current_value] = i
        #         if current_value - 1 in d:
        #             ans = max(ans, i - d[current_value - 1])
        #
        # return ans
