from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("My name is Haley", "My Haley"), Output=True))
        self.testcases.append(case(Input=("of", "A lot of words"), Output=False))
        self.testcases.append(case(Input=("Eating right now", "Eating"), Output=True))
        self.testcases.append(case(Input=("Luky", "Lucccky"), Output=False))

    def get_testcases(self):
        return self.testcases
