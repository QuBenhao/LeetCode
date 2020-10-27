import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operation,type_num = test_input
        obj = None
        output = []
        for i in range(len(operation)):
            if operation[i] == "ParkingSystem":
                big,medium,small = type_num[i]
                obj = ParkingSystem(big,medium,small)
                output.append(None)
            else:
                param_1 = obj.addCar(carType=type_num[i].pop())
                output.append(param_1)
        return output


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
