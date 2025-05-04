from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 4, 1, [0, 3, 8, 10], [5, 8, 3, 6]], Output=62))
		self.testcases.append(case(Input=[5, 5, 1, [0, 1, 2, 3, 5], [8, 3, 9, 3, 3]], Output=34))
		self.testcases.append(case(Input=[3, 3, 1, [0, 1, 3], [1,3,1]], Output=3))
		self.testcases.append(case(Input=[4, 4, 1, [0, 1, 2, 4], [2, 1, 3, 3]], Output=5))
		self.testcases.append(case(Input=[4, 4, 2, [0, 1, 3, 4], [2, 1, 2, 5]], Output=8))
		self.testcases.append(case(Input=[4, 4, 2, [0, 2, 3, 4], [2, 2, 3, 1]], Output=8))

	def get_testcases(self):
		return self.testcases
