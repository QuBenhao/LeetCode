import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTime(str(test_input))

    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        sb = []
        sb.append(time[0] if time[0] != '?' else '2' if time[1] == '?' or time[1] < '4' else '1')
        sb.append(time[1] if time[1] != '?' else '3' if sb[0] == '2' else '9')
        sb.append(':')
        sb.append('5' if time[3] == '?' else time[3])
        sb.append('9' if time[4] == '?' else time[4])
        return ''.join(sb)
