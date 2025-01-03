from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=1, Output=10))
		self.testcases.append(case(Input=2, Output=20))
		self.testcases.append(case(Input=3131, Output=136006598))

	def get_testcases(self):
		return self.testcases
