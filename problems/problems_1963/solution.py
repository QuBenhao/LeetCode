import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(str(test_input))

    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = count = 0
        for c in s:
            if c == '[':
                count += 1
            else:
                if not count:
                    # 将最右的'['和这个']'互换，后面的count会多1，但是由于数量相等，不影响再往后的右括号
                    ans += 1
                    count += 1
                else:
                    count -= 1
        return ans
