import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operations, data = test_input
        operations.pop(0)
        os = OrderedStream(data.pop(0).pop())
        result = [None]
        for d in data:
            result.append(os.insert(d[0],d[1]))
        return result

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.data = [None] * n
        self.ptr = 0

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        id -= 1
        self.data[id] = value
        if id > self.ptr:
            return []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1
        return self.data[id:self.ptr]
