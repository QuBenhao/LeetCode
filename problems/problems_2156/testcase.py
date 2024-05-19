from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['leetcode', 7, 20, 2, 0], Output="ee"))
		self.testcases.append(case(Input=['fbxzaad', 31, 100, 3, 32], Output="fbx"))

	def get_testcases(self):
		return self.testcases
