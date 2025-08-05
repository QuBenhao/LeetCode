from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 5], [3, 5, 4]], Output=1))
		self.testcases.append(case(Input=[[3, 6, 1], [6, 4, 7]], Output=0))

	def get_testcases(self):
		return self.testcases
