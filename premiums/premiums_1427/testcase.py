from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', [[0, 1], [1, 2]]], Output="cab"))
		self.testcases.append(case(Input=['abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]]], Output="efgabcd"))

	def get_testcases(self):
		return self.testcases
