from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
                                          [[1, 1, 0], [1], [2], [3], [1]]), Output=[None, True, True, False, False]))

    def get_testcases(self):
        return self.testcases
