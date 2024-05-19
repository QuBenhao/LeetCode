import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateTheBox([x[:] for x in test_input])

    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(box), len(box[0])
        ans = [['.'] * m for _ in range(n)]
        for i in range(m):
            count = 0
            for j in range(n):
                if box[i][j] == '*':
                    ans[j][m-1-i] = '*'
                    for k in range(1, count+1):
                        ans[j-k][m-1-i] = '#'
                    count = 0
                elif box[i][j] == '#':
                    count += 1
            if count:
                for k in range(count):
                    ans[n-1-k][m-1-i] = '#'
        return ans
