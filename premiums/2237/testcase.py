from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 1], [2, 1], [3, 2]], [0, 2, 1, 4, 1]], Output=4))
		self.testcases.append(case(Input=[1, [[0, 1]], [2]], Output=0))

	def get_testcases(self):
		return self.testcases
