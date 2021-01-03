import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        boxTypes, truckSize = test_input
        return self.maximumUnits([x[:] for x in boxTypes], truckSize)

    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: -x[1])
        count = 0
        weight = 0
        while boxTypes and count < truckSize:
            if boxTypes[0][0] > 0:
                boxTypes[0][0] -= 1
                count += 1
                weight += boxTypes[0][1]
            else:
                boxTypes.pop(0)
        return weight
