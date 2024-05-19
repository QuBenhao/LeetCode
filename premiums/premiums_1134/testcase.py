from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=153, Output=True))
		self.testcases.append(case(Input=123, Output=False))

	def get_testcases(self):
		return self.testcases
