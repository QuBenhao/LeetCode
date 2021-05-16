from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
                                          [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]),
                                   Output=[None, None, None, 1, -1, None, 1, None, -1]))
        self.testcases.append(case(Input=(
        ["MyHashMap", "put", "put", "remove", "get", "put", "put", "put", "remove", "put", "put", "put", "put",
         "remove", "put", "get", "put", "remove", "remove", "put", "put", "get", "put", "remove", "put", "put", "put",
         "remove", "put", "remove", "put", "put", "put", "put", "remove", "put", "remove", "put", "put", "put", "put",
         "put", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
         "put", "remove", "put", "put", "put", "put", "put", "put", "put", "remove", "put", "get", "get", "put", "put",
         "get", "put", "put", "put", "put", "put", "remove", "remove", "put", "get", "put", "put", "put", "remove",
         "put", "put", "put", "put", "put", "put", "put", "put", "put", "remove", "put", "put", "remove", "put",
         "remove"]
        , [[], [4, 30], [41, 24], [12], [4], [82, 59], [92, 22], [34, 41], [98], [59, 59], [20, 35], [24, 74], [95, 10],
           [59], [66, 1], [20], [20, 46], [59], [2], [28, 13], [45, 16], [41], [12, 8], [24], [27, 61], [43, 57],
           [72, 24], [20], [95, 75], [20], [64, 8], [36, 61], [95, 53], [76, 34], [24], [55, 68], [21], [75, 71],
           [43, 36], [50, 3], [4, 97], [44, 57], [20, 1], [4, 66], [8, 71], [14], [34, 41], [75, 64], [98, 47], [35],
           [12, 45], [93, 69], [93, 10], [64, 66], [72, 99], [53], [50, 97], [48, 65], [80], [46, 13], [60, 15],
           [42, 3], [29, 18], [95, 70], [0, 80], [6, 15], [73], [26, 45], [58], [46], [60, 91], [13, 32], [75],
           [99, 67], [85, 95], [82, 37], [7, 62], [1, 97], [66], [13], [63, 35], [65], [25, 12], [38, 69], [44, 3], [6],
           [86, 62], [76, 8], [22, 79], [55, 86], [37, 79], [63, 26], [51, 23], [48, 50], [77, 72], [65], [14, 18],
           [63, 90], [37], [88, 6], [61]]),
                                   Output=[None, None, None, None, 30, None, None, None, None, None, None, None, None,
                                           None, None, 35, None, None, None, None, None, 24, None, None, None, None,
                                           None, None, None, None, None, None, None, None, None, None, None, None, None,
                                           None, None, None, None, None, None, -1, None, None, None, -1, None, None,
                                           None, None, None, -1, None, None, None, None, None, None, None, None, None,
                                           None, None, None, -1, 13, None, None, 64, None, None, None, None, None, None,
                                           None, None, -1, None, None, None, None, None, None, None, None, None, None,
                                           None, None, None, None, None, None, None, None, None]))

    def get_testcases(self):
        return self.testcases
