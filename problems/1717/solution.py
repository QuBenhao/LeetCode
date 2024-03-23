import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumGain(*test_input)

    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def cal(a_, b_, m):
            if not a_ or not b_:
                return 0
            total = 0
            i = len(a_)
            for j in range(len(b_) - 1, -1, -1):
                i = i - 1
                while i >= 0 and a_[i] > b_[j]:
                    i -= 1
                if i == -1:
                    break
                b_.pop(j)
                a_.pop(i)
                total += m
            return total

        a_list = []
        b_list = []
        ans = 0
        s += 'c'
        for k in range(len(s)):
            if s[k] == 'a':
                a_list.append(k)
            elif s[k] == 'b':
                b_list.append(k)
            else:
                if x > y:
                    ans += cal(a_list, b_list, x)
                    ans += cal(b_list, a_list, y)
                else:
                    ans += cal(b_list, a_list, y)
                    ans += cal(a_list, b_list, x)
                a_list = []
                b_list = []
        return ans
