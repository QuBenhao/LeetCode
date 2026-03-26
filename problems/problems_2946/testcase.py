from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4], Output=False))
		self.testcases.append(case(Input=[[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2], Output=True))
		self.testcases.append(case(Input=[[[2, 2], [2, 2]], 3], Output=True))
		self.testcases.append(case(Input=[[[15, 15, 8]],1], Output=False))

	def get_testcases(self):
		return self.testcases
