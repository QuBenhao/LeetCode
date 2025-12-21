from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], [1, 1, 1]], Output=4))
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], [3, 2, 3]], Output=2))
		self.testcases.append(case(Input=[4, [[0, 1], [0, 2], [0, 3]], [1, 1, 4, 4]], Output=3))
		self.testcases.append(case(Input=[2, [[0, 1]], [9, 8]], Output=0))

	def get_testcases(self):
		return self.testcases
