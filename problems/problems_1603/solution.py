import solution
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ParkingSystem(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


# class ParkingSystem(object):
#
#     def __init__(self, big, medium, small):
#         """
#         :type big: int
#         :type medium: int
#         :type small: int
#         """
#         self.big = big
#         self.medium = medium
#         self.small = small
#
#     def addCar(self, carType):
#         """
#         :type carType: int
#         :rtype: bool
#         """
#         if carType == 1 and self.big > 0:
#             self.big -= 1
#             return True
#         elif carType == 2 and self.medium > 0:
#             self.medium -= 1
#             return True
#         elif carType == 3 and self.small > 0:
#             self.small -= 1
#             return True
#         return False


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spot = [0, big, medium, small]


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.spot[carType]:
            self.spot[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
