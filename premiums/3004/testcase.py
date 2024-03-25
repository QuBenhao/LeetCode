from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [0, 3]], [1, 1, 2, 3]], Output=1))
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [0, 3]], [1, 1, 1, 1]], Output=4))
		self.testcases.append(case(Input=[[[0, 1], [0, 2], [2, 3], [2, 4]], [1, 2, 3, 3, 3]], Output=3))

	def get_testcases(self):
		return self.testcases
