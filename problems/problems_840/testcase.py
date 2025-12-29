from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], Output=1))
		self.testcases.append(case(Input=[[8]], Output=0))

	def get_testcases(self):
		return self.testcases
