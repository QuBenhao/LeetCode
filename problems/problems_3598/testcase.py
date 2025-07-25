from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['jump', 'run', 'run', 'jump', 'run'], Output=[3, 0, 0, 3, 3]))
		self.testcases.append(case(Input=['dog', 'racer', 'car'], Output=[0, 0, 0]))
		self.testcases.append(case(Input=["cdbff"], Output=[0]))

	def get_testcases(self):
		return self.testcases
