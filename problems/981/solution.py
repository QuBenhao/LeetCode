import solution
from collections import defaultdict
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, vals = test_input
        obj = TimeMap()
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "set":
                obj.set(vals[i][0], vals[i][1], vals[i][2])
                ans.append(None)
            else:
                ans.append(obj.get(vals[i][0], vals[i][1]))
        return ans


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = defaultdict(list)
        self.vals = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.times[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.times:
            return ""
        idx = bisect.bisect_right(self.times[key], timestamp)
        return self.vals[key][idx-1] if idx else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
