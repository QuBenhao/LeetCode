from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[6, 10], [5, 15]], Output=2))
		self.testcases.append(case(Input=[[1, 3], [10, 20], [2, 5], [4, 8]], Output=4))

	def get_testcases(self):
		return self.testcases
