from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3], [3, 2, 1]), Output=14))
        self.testcases.append(case(Input=([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]), Output=102))
        self.testcases.append(case(Input=(
        [-854, -941, 10, 299, 995, -346, 294, -393, 351, -76, 210, 897, -651, 920, 624, 969, -629, 985, -695, 236, 637,
         -901, -817, 546, -69, 192, -377, 251, 542, -316, -879, -764, -560, 927, 629, 877, 42, 381, 367, -549, 602, 139,
         -312, -281, 105, 690, -376, -705, -906, 85, -608, 639, 752, 770, -139, -601, 341, 61, 969, 276, 176, -715,
         -545, 471, -170, -126, 596, -737, 130]
        , [83, 315, -442, -714, 461, 920, -737, -93, -818, -760, 558, -584, -358, -228, -220]), Output=
                                   3040819))

    def get_testcases(self):
        return self.testcases
