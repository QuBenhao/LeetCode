import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.balancedStringSplit(test_input)

    def balancedStringSplit(self, s: str) -> int:
        count = 0
        cur_count = 0
        for c in s:
            if cur_count == 0:
                cur = c
            if c == cur:
                cur_count += 1
            elif cur_count > 0:
                cur_count -= 1
                if cur_count == 0:
                    count += 1
        return count
