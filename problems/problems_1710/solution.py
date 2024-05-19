import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumUnits(*test_input)

    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: -x[1])
        count = 0
        weight = 0
        for i in range(len(boxTypes)):
            if boxTypes[i][0] + count >= truckSize:
                weight += (truckSize - count) * boxTypes[i][1]
                return weight
            else:
                weight += boxTypes[i][0] * boxTypes[i][1]
                count += boxTypes[i][0]
        return weight
