import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.evaluate(*test_input)

    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = dict()
        for k,v in knowledge:
            d[k] = v
        ans = ""
        isKey = False
        key = ""
        for c in s:
            if c == '(':
                isKey = True
            elif c == ')':
                isKey = False
                if key in d:
                    ans += d[key]
                else:
                    ans += '?'
                key = ""
            elif not isKey:
                ans += c
            else:
                key += c
        return ans
