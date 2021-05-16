import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, values = test_input
        ops.pop(0)
        values.pop(0)
        obj = FreqStack()
        ans = [None]
        for i in range(len(ops)):
            if ops[i] == "push":
                ans.append(obj.push(values[i][0]))
            else:
                ans.append(obj.pop())
        return ans


class FreqStack(object):

    def __init__(self):
        from collections import Counter
        self.freq = []
        self.frequency = Counter()
        self.len = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        import heapq
        self.frequency[x] += 1
        heapq.heappush(self.freq, (-self.frequency[x],-self.len,x))
        self.len += 1

    def pop(self):
        """
        :rtype: int
        """
        import heapq
        val = heapq.heappop(self.freq)[2]
        self.frequency[val] -= 1
        return val
