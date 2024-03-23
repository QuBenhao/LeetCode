import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMatches(*test_input)

    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey == "type":
            i = 0
        elif ruleKey == "color":
            i = 1
        else:
            i = 2
        return [item[i] for item in items].count(ruleValue)

        # ans = 0
        # for ty, color, name in items:
        #     if ruleKey == "type" and ty == ruleValue:
        #         ans += 1
        #     elif ruleKey == "color" and color == ruleValue:
        #         ans += 1
        #     elif ruleKey == "name" and name == ruleValue:
        #         ans += 1
        # return ans
