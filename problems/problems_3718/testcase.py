from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[8, 2, 3, 4, 6], 2], Output=10))
		self.testcases.append(case(Input=[[1, 4, 7, 10, 15], 5], Output=5))

	def get_testcases(self):
		return self.testcases
