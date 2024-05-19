import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkPartitioning(str(test_input))

    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        partition = [[False] * n for _ in range(n)]
        left = []
        right = []
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                # partition has to be at least start equal to end
                if s[i] == s[j]:
                    # dp: if (i+1,j-1) is palindrome, then (i,j) is palindrome
                    if j - i >= 2:
                        partition[i][j] = partition[i+1][j-1]
                    # a or aba is palindrome
                    else:
                        partition[i][j] = True

                    # split into three sub palindrome strings,
                    # has to be one start at beginning and one end at the end
                    if i == 0 and partition[i][j]:
                        left.append(j)
                    if j == n-1 and partition[i][j]:
                        right.append(i)

        for i in left:
            for j in right:
                # we know that partition[0][i] is True and partition[j][n-1] is True
                if partition[i+1][j-1]:
                    return True

        return False
