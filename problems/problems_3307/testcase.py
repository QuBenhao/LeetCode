from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [0, 0, 0]], Output="a"))
		self.testcases.append(case(Input=[10, [0, 1, 0, 1]], Output="b"))

	def get_testcases(self):
		return self.testcases
