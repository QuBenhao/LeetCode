import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, nums = test_input
        # Your MyQueue object will be instantiated and called as such:
        obj = TripleInOne(nums[0][0])
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "push":
                obj.push(nums[i][0],nums[i][1])
                ans.append(None)
            elif ops[i] == "pop":
                ans.append(obj.pop(nums[i][0]))
            elif ops[i] == "peek":
                ans.append(obj.peek(nums[i][0]))
            else:
                ans.append(obj.isEmpty(nums[i][0]))
        return ans


class TripleInOne(object):

    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        self.max = stackSize
        self.data = [0] * stackSize * 3 + [[0, stackSize, stackSize * 2]]

    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        if self.data[-1][stackNum] == self.max * (stackNum + 1):
            return -1
        self.data[self.data[-1][stackNum]] = value
        self.data[-1][stackNum] += 1

    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        if self.data[-1][stackNum] == self.max * stackNum:
            return -1
        self.data[-1][stackNum] -= 1
        return self.data[self.data[-1][stackNum]]

    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        if self.data[-1][stackNum] == self.max * stackNum:
            return -1
        return self.data[self.data[-1][stackNum] - 1]

    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        return self.data[-1][stackNum] == self.max * stackNum

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
