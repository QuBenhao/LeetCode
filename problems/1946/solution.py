import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumNumber(*test_input)

    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        ans = []
        changed = False
        for i,c in enumerate(num):
            t = int(c)
            if change[t] > t:
                changed = True
                ans.append(str(change[t]))
            elif change[t] == t:
                ans.append(c)
            else:
                if changed:
                    ans.append(num[i:])
                    break
                ans.append(c)
        return ''.join(ans)
