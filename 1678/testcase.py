from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="G()(al)", Output="Goal"))
        self.testcases.append(case(Input="G()()()()(al)", Output="Gooooal"))
        self.testcases.append(case(Input="(al)G(al)()()G", Output="alGalooG"))

    def get_testcases(self):
        return self.testcases
