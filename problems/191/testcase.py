from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=11, Output=3))
		self.testcases.append(case(Input=128, Output=1))
		self.testcases.append(case(Input=2147483645, Output=30))

	def get_testcases(self):
		return self.testcases
