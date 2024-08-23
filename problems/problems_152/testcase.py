from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, -2, 4], Output=6))
		self.testcases.append(case(Input=[-2, 0, -1], Output=0))

	def get_testcases(self):
		return self.testcases
