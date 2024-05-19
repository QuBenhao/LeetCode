from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]], 3], Output=17))
		self.testcases.append(case(Input=[4, [[0, 1, 3], [2, 3, 2]], 2], Output=-1))

	def get_testcases(self):
		return self.testcases
