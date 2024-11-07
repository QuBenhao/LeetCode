from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 4, [[2, 1, 1]]], Output=True))
		self.testcases.append(case(Input=[3, 3, [[1, 1, 2]]], Output=False))
		self.testcases.append(case(Input=[3, 3, [[2, 1, 1], [1, 2, 1]]], Output=False))
		self.testcases.append(case(Input=[4, 4, [[5, 5, 1]]], Output=True))

	def get_testcases(self):
		return self.testcases
