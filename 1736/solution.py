import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTime(str(test_input))

    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ans = ""

        if time[0] == '?':
            if time[1] == '?':
                ans += '23'
            elif time[1] >= '4':
                ans += '1' + time[1]
            else:
                ans += '2' + time[1]
        elif time[1] == '?':
            if time[0] < '2':
                ans += time[0] + '9'
            else:
                ans += '23'
        else:
            ans += time[0:2]
        ans += ':'
        if time[3] == '?':
            ans += '5'
        else:
            ans += time[3]
        if time[4] == '?':
            ans += '9'
        else:
            ans += time[4]
        return ans
