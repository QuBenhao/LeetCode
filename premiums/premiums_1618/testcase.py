from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['helloworld', 80, 20, [6, 8, 10, 12, 14, 16, 18, 24, 36]], Output=6))
		self.testcases.append(case(Input=['leetcode', 1000, 50, [1, 2, 4]], Output=4))
		self.testcases.append(case(Input=['easyquestion', 100, 100, [10, 15, 20, 25]], Output=-1))

	def get_testcases(self):
		return self.testcases
