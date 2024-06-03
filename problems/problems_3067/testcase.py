from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1], Output=[0, 4, 6, 6, 4, 0]))
		self.testcases.append(case(Input=[[[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], 3], Output=[2, 0, 0, 0, 0, 0, 2]))

	def get_testcases(self):
		return self.testcases
