from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 16], [2, 8], [1, 6], [7, 12]], Output=2))
		self.testcases.append(case(Input=[[1, 2], [3, 4], [5, 6], [7, 8]], Output=4))
		self.testcases.append(case(Input=[[1, 2], [2, 3], [3, 4], [4, 5]], Output=2))

	def get_testcases(self):
		return self.testcases
