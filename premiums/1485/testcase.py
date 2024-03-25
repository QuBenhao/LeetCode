from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, None], None, [4, 3], [7, 0]], Output=[[1, None], None, [4, 3], [7, 0]]))
		self.testcases.append(case(Input=[[1, 4], None, [1, 0], None, [1, 5], [1, 5]], Output=[[1, 4], None, [1, 0], None, [1, 5], [1, 5]]))
		self.testcases.append(case(Input=[[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]], Output=[[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]]))

	def get_testcases(self):
		return self.testcases
