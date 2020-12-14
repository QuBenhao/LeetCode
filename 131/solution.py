import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partition(test_input)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palindrome = set()

        def is_palindrome(string):
            if string in palindrome:
                return True
            n = len(string)
            for i in range(n):
                if i >= n - 1 - i:
                    palindrome.add(string)
                    return True
                if string[i] != string[n - 1 - i]:
                    return False

        def dfs(curr_list, s_left):
            if not s_left:
                ans.append(curr_list)
                return

            for i in range(len(s_left)):
                if is_palindrome(s_left[:i + 1]):
                    cp = curr_list.copy()
                    cp.append(s_left[:i + 1])
                    dfs(cp, s_left[i + 1:])

        ans = []

        dfs([], s)
        return ans
