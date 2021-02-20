import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.romanToInt(str(test_input))

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        last = 0
        ans = 0

        for c in s:
            curr = roman_dict[c]
            if last < curr:
                ans -= last * 2
            ans += curr
            last = curr

        # for i in range(len(s)-1,-1,-1):
        #     if last and roman_dict[last] > roman_dict[s[i]]:
        #         ans -= roman_dict[s[i]]
        #     else:
        #         ans += roman_dict[s[i]]
        #     last = s[i]

        return ans
