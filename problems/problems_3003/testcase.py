from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['accca', 2], Output=3))
		self.testcases.append(case(Input=['aabaab', 3], Output=1))
		self.testcases.append(case(Input=['xxyz', 1], Output=4))

	def get_testcases(self):
		return self.testcases
