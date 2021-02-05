import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.simplifyPath(str(test_input))

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ans = []
        paths = path.split("/")
        for p in paths:
            if p == "..":
                if ans:
                    ans.pop()
            elif p and p != ".":
                ans.append(p)
        return "/" + '/'.join(ans)
