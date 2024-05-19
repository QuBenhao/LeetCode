import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(str(test_input))

    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n
        curr, steps = 0, 0
        for i in range(n):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        curr, steps = 0, 0
        for i in reversed(range(n)):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        return answer
