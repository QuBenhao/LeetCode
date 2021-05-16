from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]), Output="bobistwoyearsold"))
        self.testcases.append(case(Input=("hi(name)", [["a", "b"]]), Output="hi?"))
        self.testcases.append(case(Input=("(a)(a)(a)aaa", [["a", "yes"]]), Output="yesyesyesaaa"))

    def get_testcases(self):
        return self.testcases
